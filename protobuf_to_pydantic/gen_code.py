import inspect
import pathlib
import sys
import time
from collections import deque
from enum import IntEnum
from types import ModuleType
from typing import _GenericAlias  # type: ignore
from typing import Any, Deque, Optional, Set, Tuple, Type

from pydantic import BaseModel
from pydantic.fields import FieldInfo

from protobuf_to_pydantic.get_desc.from_pgv import customer_validator


def _get_type_name(type_: Type) -> str:
    type_name: str = repr(type_)
    type_module = inspect.getmodule(type_)
    if type_module and type_module.__name__ == "builtins" or inspect.isfunction(type_module):
        type_name = type_.__name__
    type_name = type_name.replace("'", '"')
    # Compatible with datetime.* name
    type_name = type_name.replace("datetime.", "")
    return type_name


class P2C(object):
    """
    BaseModel objects into corresponding Python code
    (only protobuf-generated pydantic.BaseModel objects are supported, not overly complex pydantic.BaseModel)
    """

    def __init__(
        self,
        *model: Type[BaseModel],
        customer_import_set: Optional[Set[str]] = None,
        customer_deque: Optional[Deque] = None,
        module_path: str = "",
        enable_autoflake: bool = True,
        enable_isort: bool = True,
        enable_yapf: bool = True,
    ):
        self._model_list: Tuple[Type[BaseModel], ...] = model
        self._import_set: Set[str] = customer_import_set or set()
        self._content_deque: Deque = customer_deque or deque()

        # init module_path
        if module_path:
            module_path_obj: pathlib.Path = pathlib.Path(module_path).absolute()
            if not module_path_obj.is_dir():
                raise TypeError(f"{module_path} must dir")
            cnt: int = 0
            while True:
                if not module_path_obj.name == "..":
                    break
                module_path_obj = module_path_obj.parent
                cnt += 1
            for _ in range(cnt):
                module_path_obj = module_path_obj.parent
            module_path = str(module_path_obj.absolute())
        self._module_path: str = module_path

        self._enable_autoflake: bool = enable_autoflake
        self._enable_isort: bool = enable_isort
        self._enable_yapf: bool = enable_yapf
        for _model in self._model_list:
            self._gen_pydantic_model_py_code(_model)

    @property
    def content(self) -> str:

        content_str: str = (
            "# This is an automatically generated file, please do not change\n"
            "# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)\n"
            f"# gen timestamp:{int(time.time())}\n\n"
        )

        content_str += "\n".join(sorted(self._import_set))
        if self._content_deque:
            _content_set: Set[str] = set()
            content_str += "\n\n"
            for content in self._content_deque:
                if content in _content_set:
                    continue
                _content_set.add(content)
                content_str += f"\n\n{content}"

        if self._enable_isort:
            try:
                import isort
            except ImportError:
                pass
            else:
                content_str = isort.code(content_str)

        if self._enable_autoflake:
            try:
                import autoflake
            except ImportError:
                pass
            else:
                content_str = autoflake.fix_code(content_str)

        if self._enable_yapf:
            try:
                from yapf.yapflib.yapf_api import FormatCode
            except ImportError:
                pass
            else:
                content_str, _ = FormatCode(content_str)

        # TODO Waiting for black development API
        # https://github.com/psf/black/issues/779
        return content_str

    @staticmethod
    def _pydantic_config_handle(model: Type[BaseModel], indent: int = 0) -> str:
        config_str: str = ""
        if not getattr(model.Config, "__p2p_dict__", None):
            return config_str
        for key, value in model.Config.__p2p_dict__.items():
            config_str += f"{' ' * (indent + 4)}{key} = {value}\n"
        if config_str:
            config_str = f"{' ' * indent}class Config:\n" + config_str
        return config_str

    def _gen_pydantic_model_py_code(self, model: Type[BaseModel]) -> None:
        self._import_set.add("from pydantic import BaseModel")
        class_str: str = f"class {model.__name__}(BaseModel):\n"
        config_class: str = self._pydantic_config_handle(model, indent=4)
        if config_class:
            class_str += config_class + "\n"
        for key, value in model.__fields__.items():
            value_type = value.outer_type_
            value_type_name: str = getattr(value_type, "__name__", None)

            # Type Hint handler
            if value.outer_type_.__module__ != "builtins":
                if inspect.isclass(value.type_) and issubclass(value.type_, IntEnum):
                    # Parse protobuf enum
                    self._import_set.add("from enum import IntEnum")
                    depend_set_str = f"class {value.type_.__name__}(IntEnum):\n"
                    for enum_name, enum_value in value.type_.__members__.items():
                        depend_set_str += " " * 4 + f"{enum_name} = {enum_value.value}\n"
                    self._content_deque.append(depend_set_str)
                else:
                    # It is not necessary to consider other types since
                    # it is converted from the message object generated by protobuf
                    value_type = model.__annotations__[key]
                    self._parse_type(value_type)
                # Extracting the exact Type Hint text
                if isinstance(value_type, _GenericAlias):
                    value_type_name = (
                        f"typing.{value_type._name}[{', '.join([i.__name__ for i in value_type.__args__])}]"
                    )
                else:
                    value_type_name = getattr(value_type, "__name__", None)

            field_str: str = self._field_info_handle(value.field_info)
            class_str = class_str + " " * 4 + f"{key}: {value_type_name} = {field_str}\n"

        validator_str: str = self._pgv_validator_handle(model)
        if validator_str:
            class_str += f"\n{validator_str}"
        self._content_deque.append(class_str)

    def _parse_type(self, type_: Any) -> None:
        type_module: Optional[ModuleType] = inspect.getmodule(type_)
        if not type_module:
            if isinstance(type_, list):
                for i in type_:
                    self._parse_type(i)
            elif isinstance(type_, dict):
                for i in type_.values():
                    self._parse_type(i)
            else:
                return

        elif getattr(type_module, "__name__", "builtins") == "builtins":
            return
        elif isinstance(type_, _GenericAlias):
            # type hint handle
            self._import_set.add("import typing")
            for type_ in type_.__args__:
                self._parse_type(type_)
            return
        elif isinstance(type_, type) and inspect.isclass(type_) and issubclass(type_, BaseModel):
            # pydantic.BaseModel handle
            self._gen_pydantic_model_py_code(type_)
        else:
            # other type handle
            if type_module.__name__ == "__main__":
                start_path: str = sys.path[0]
                if self._module_path:
                    module_name = self._module_path.split("/")[-1] + type_module.__file__.replace(self._module_path, "")
                else:
                    # Find the name of the module for the variable that starts the code file
                    if not type_module.__file__.startswith(start_path):
                        # Compatible scripts are run directly in the submodule
                        module_name = f"{start_path.split('/')[-1]}.{type_module.__file__.split('/')[-1]}"
                    else:
                        module_name = start_path.split("/")[-1] + type_module.__file__.replace(start_path, "")
                module_name = module_name.replace("/", ".").replace(".py", "")

                class_name: str = _get_type_name(type_)
            else:
                module_name = type_module.__name__
                if inspect.isclass(type_):
                    class_name = type_.__name__
                elif not inspect.isfunction(type_):
                    class_name = type_.__class__.__name__
                else:
                    class_name = type_.__name__

            if module_name.startswith("google.protobuf"):
                self._import_set.add(f"from {module_name} import {class_name}  # type: ignore")
            else:
                self._import_set.add(f"from {module_name} import {class_name}")

    def _field_info_handle(self, field_info: FieldInfo) -> str:
        # Introduce the corresponding class for FieldInfo's properties
        self._import_set.add(f"from {field_info.__module__} import {field_info.__class__.__name__}")
        field_list = []
        for k, v in field_info.__repr_args__():
            if k == "default" and str(v) == "PydanticUndefined":
                # Ignore the default value of the pydantic field
                continue
            if k == "extra" and not v:
                # Ignore cases where the value of extra is empty
                continue

            value_name: str = _get_type_name(v)
            field_list.append(f"{k}={value_name}")
            self._parse_type(v)

        return f"{field_info.__class__.__name__}({', '.join(field_list)})"

    def _pgv_validator_handle(self, model: Type[BaseModel]) -> str:
        validator_str: str = ""
        for key, value in model.__fields__.items():
            if not value.class_validators:
                continue
            for class_validator_key, class_validator_value in value.class_validators.items():
                if class_validator_value.func.__module__ != customer_validator.__name__:
                    # TODO Here currently only consider the support for pgv, the follow-up to fill in
                    continue
                self._import_set.add("from pydantic import validator")
                self._import_set.add(
                    f"from {class_validator_value.func.__module__} import {class_validator_value.func.__name__}"
                )
                validator_str += (
                    f"{' ' * 4}"
                    f"{class_validator_key}_{key} = validator("
                    f"'{key}', allow_reuse=True)({class_validator_value.func.__name__})\n"
                )
        return validator_str


def pydantic_model_to_py_code(
    *model: Type[BaseModel],
    customer_import_set: Optional[Set[str]] = None,
    customer_deque: Optional[Deque] = None,
    module_path: str = "",
    enable_autoflake: bool = True,
    enable_isort: bool = True,
    enable_yapf: bool = True,
) -> str:
    return P2C(
        *model,
        customer_import_set=customer_import_set,
        customer_deque=customer_deque,
        module_path=module_path,
        enable_autoflake=enable_autoflake,
        enable_isort=enable_isort,
        enable_yapf=enable_yapf,
    ).content


def pydantic_model_to_py_file(
    filename: str,
    *model: Type[BaseModel],
    customer_import_set: Optional[Set[str]] = None,
    customer_deque: Optional[Deque] = None,
    open_mode: str = "w",
    module_path: str = "",
    enable_autoflake: bool = True,
    enable_isort: bool = True,
    enable_yapf: bool = True,
) -> None:
    with open(filename, mode=open_mode) as f:
        f.write(
            pydantic_model_to_py_code(
                *model,
                customer_import_set=customer_import_set,
                customer_deque=customer_deque,
                module_path=module_path,
                enable_autoflake=enable_autoflake,
                enable_isort=enable_isort,
                enable_yapf=enable_yapf,
            )
        )