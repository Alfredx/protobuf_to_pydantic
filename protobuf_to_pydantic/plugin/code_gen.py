import importlib
import logging
import pathlib
import sys

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse
from mypy_protobuf.main import Descriptors, code_generation

from protobuf_to_pydantic.plugin.config import ConfigModel, get_config_by_module

# If want to parse option, need to import the corresponding file
#   see details:https://stackoverflow.com/a/59301849
from protobuf_to_pydantic.protos import p2p_validate_pb2  # isort:skip
from protobuf_to_pydantic.protos import validate_pb2  # isort:skip


logger = logging.getLogger(__name__)


class CodeGen(object):
    config: ConfigModel

    def __init__(self) -> None:
        self.param_dict: dict = {}
        with code_generation() as (request, response):
            self.parse_param(request)
            self.gen_config()
            self.generate_pydantic_model(Descriptors(request), response)

    def parse_param(self, request: CodeGeneratorRequest) -> None:
        if not request.parameter:
            return
        try:
            for one_param_str in request.parameter.split(","):
                k, v = one_param_str.split("=")
                self.param_dict[k] = v
        except Exception as e:
            logger.exception(e)
            print(f"parse command-line error:{e}", file=sys.stderr)
        print(f"Parse command-line arguments:{self.param_dict}", file=sys.stderr)

    def gen_config(self) -> None:
        if "config_path" not in self.param_dict:
            self.config = ConfigModel()
        else:
            path_obj: pathlib.Path = pathlib.Path(self.param_dict["config_path"]).absolute()
            if not path_obj.exists():
                raise SystemError(f"Can not  find config file at {path_obj}")

            print(f"Load config: {str(path_obj)}", file=sys.stderr)
            self.config = get_config_by_module(
                importlib.import_module(f"{path_obj.parent.name}.{path_obj.name.replace('.py', '')}")
            )

    def generate_pydantic_model(self, descriptors: Descriptors, response: CodeGeneratorResponse) -> None:
        for name, fd in descriptors.to_generate.items():
            if fd.package in self.config.ignore_pkg_list:
                continue
            file = response.file.add()
            file.name = fd.name[:-6].replace("-", "_").replace(".", "/") + "_p2p.py"
            file.content = self.config.file_descriptor_proto_to_code(
                fd=fd, descriptors=descriptors, config=self.config
            ).content
            print(f"Writing protobuf-to-pydantic code to {file.name}", file=sys.stderr)