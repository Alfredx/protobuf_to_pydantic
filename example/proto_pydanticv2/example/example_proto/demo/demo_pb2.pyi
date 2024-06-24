"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import example.example_proto.common.single_pb2
import google.protobuf.descriptor
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SexType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SexTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SexType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    man: _SexType.ValueType  # 0
    women: _SexType.ValueType  # 1

class SexType(_SexType, metaclass=_SexTypeEnumTypeWrapper): ...

man: SexType.ValueType  # 0
women: SexType.ValueType  # 1
global___SexType = SexType

class UserMessage(google.protobuf.message.Message):
    """user info"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UID_FIELD_NUMBER: builtins.int
    AGE_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    SEX_FIELD_NUMBER: builtins.int
    DEMO_FIELD_NUMBER: builtins.int
    IS_ADULT_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    DEMO_MESSAGE_FIELD_NUMBER: builtins.int
    uid: builtins.str
    """p2p: {"required": true, "example": "10086", "title": "UID", "description": "user union id"}"""
    age: builtins.int
    """p2p: {"example": 18, "title": "use age", "ge": 0}"""
    height: builtins.float
    """p2p: {"ge": 0, "le": 2.5}"""
    sex: global___SexType.ValueType
    demo: example.example_proto.common.single_pb2.DemoEnum.ValueType
    is_adult: builtins.bool
    user_name: builtins.str
    """p2p: {"description": "user name"}
    p2p: {"default": "", "min_length": 1, "max_length": "10", "example": "so1n"}
    """
    @property
    def demo_message(self) -> example.example_proto.common.single_pb2.DemoMessage:
        """p2p: {"extra": {"customer_string": "c1", "customer_int": 1}}"""
    def __init__(
        self,
        *,
        uid: builtins.str = ...,
        age: builtins.int = ...,
        height: builtins.float = ...,
        sex: global___SexType.ValueType = ...,
        demo: example.example_proto.common.single_pb2.DemoEnum.ValueType = ...,
        is_adult: builtins.bool = ...,
        user_name: builtins.str = ...,
        demo_message: example.example_proto.common.single_pb2.DemoMessage | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["demo_message", b"demo_message"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["age", b"age", "demo", b"demo", "demo_message", b"demo_message", "height", b"height", "is_adult", b"is_adult", "sex", b"sex", "uid", b"uid", "user_name", b"user_name"]) -> None: ...

global___UserMessage = UserMessage

class OtherMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    DOUBLE_VALUE_FIELD_NUMBER: builtins.int
    FIELD_MASK_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> google.protobuf.struct_pb2.Struct: ...
    @property
    def double_value(self) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def field_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    def __init__(
        self,
        *,
        metadata: google.protobuf.struct_pb2.Struct | None = ...,
        double_value: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
        field_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_field_mask", b"_field_mask", "double_value", b"double_value", "field_mask", b"field_mask", "metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_field_mask", b"_field_mask", "double_value", b"double_value", "field_mask", b"field_mask", "metadata", b"metadata"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_field_mask", b"_field_mask"]) -> typing_extensions.Literal["field_mask"] | None: ...

global___OtherMessage = OtherMessage

class MapMessage(google.protobuf.message.Message):
    """test map message and bad message"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class UserMapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___UserMessage: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___UserMessage | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    class UserFlagEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bool
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    USER_MAP_FIELD_NUMBER: builtins.int
    USER_FLAG_FIELD_NUMBER: builtins.int
    @property
    def user_map(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___UserMessage]: ...
    @property
    def user_flag(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.bool]: ...
    def __init__(
        self,
        *,
        user_map: collections.abc.Mapping[builtins.str, global___UserMessage] | None = ...,
        user_flag: collections.abc.Mapping[builtins.str, builtins.bool] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_flag", b"user_flag", "user_map", b"user_map"]) -> None: ...

global___MapMessage = MapMessage

class RepeatedMessage(google.protobuf.message.Message):
    """test repeated msg"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STR_LIST_FIELD_NUMBER: builtins.int
    INT_LIST_FIELD_NUMBER: builtins.int
    USER_LIST_FIELD_NUMBER: builtins.int
    @property
    def str_list(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """p2p: {"min_items": 3, "max_items": 5}"""
    @property
    def int_list(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """p2p: {"min_items": 1, "max_items": 5, "unique_items": true}"""
    @property
    def user_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UserMessage]: ...
    def __init__(
        self,
        *,
        str_list: collections.abc.Iterable[builtins.str] | None = ...,
        int_list: collections.abc.Iterable[builtins.int] | None = ...,
        user_list: collections.abc.Iterable[global___UserMessage] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["int_list", b"int_list", "str_list", b"str_list", "user_list", b"user_list"]) -> None: ...

global___RepeatedMessage = RepeatedMessage

class NestedMessage(google.protobuf.message.Message):
    """test nested message"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _IncludeEnum:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _IncludeEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[NestedMessage._IncludeEnum.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        zero: NestedMessage._IncludeEnum.ValueType  # 0
        one: NestedMessage._IncludeEnum.ValueType  # 1
        two: NestedMessage._IncludeEnum.ValueType  # 2

    class IncludeEnum(_IncludeEnum, metaclass=_IncludeEnumEnumTypeWrapper): ...
    zero: NestedMessage.IncludeEnum.ValueType  # 0
    one: NestedMessage.IncludeEnum.ValueType  # 1
    two: NestedMessage.IncludeEnum.ValueType  # 2

    class UserPayMessage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        BANK_NUMBER_FIELD_NUMBER: builtins.int
        EXP_FIELD_NUMBER: builtins.int
        UUID_FIELD_NUMBER: builtins.int
        bank_number: builtins.str
        """p2p: {"type": "p2p@import|pydantic.types|PaymentCardNumber"}"""
        @property
        def exp(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """p2p: {"default_factory": "p2p@local|exp_time"}"""
        uuid: builtins.str
        """p2p: {"default_factory": "p2p@local|uuid4"}"""
        def __init__(
            self,
            *,
            bank_number: builtins.str = ...,
            exp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
            uuid: builtins.str = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["exp", b"exp"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["bank_number", b"bank_number", "exp", b"exp", "uuid", b"uuid"]) -> None: ...

    class UserListMapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___RepeatedMessage: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___RepeatedMessage | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    class UserMapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___MapMessage: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___MapMessage | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    USER_LIST_MAP_FIELD_NUMBER: builtins.int
    USER_MAP_FIELD_NUMBER: builtins.int
    USER_PAY_FIELD_NUMBER: builtins.int
    INCLUDE_ENUM_FIELD_NUMBER: builtins.int
    NOT_ENABLE_USER_PAY_FIELD_NUMBER: builtins.int
    EMPTY_FIELD_NUMBER: builtins.int
    AFTER_REFER_FIELD_NUMBER: builtins.int
    @property
    def user_list_map(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___RepeatedMessage]: ...
    @property
    def user_map(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___MapMessage]: ...
    @property
    def user_pay(self) -> global___NestedMessage.UserPayMessage: ...
    include_enum: global___NestedMessage.IncludeEnum.ValueType
    @property
    def not_enable_user_pay(self) -> global___NestedMessage.UserPayMessage:
        """p2p: {"enable": false}"""
    @property
    def empty(self) -> google.protobuf.empty_pb2.Empty: ...
    @property
    def after_refer(self) -> global___AfterReferMessage: ...
    def __init__(
        self,
        *,
        user_list_map: collections.abc.Mapping[builtins.str, global___RepeatedMessage] | None = ...,
        user_map: collections.abc.Mapping[builtins.str, global___MapMessage] | None = ...,
        user_pay: global___NestedMessage.UserPayMessage | None = ...,
        include_enum: global___NestedMessage.IncludeEnum.ValueType = ...,
        not_enable_user_pay: global___NestedMessage.UserPayMessage | None = ...,
        empty: google.protobuf.empty_pb2.Empty | None = ...,
        after_refer: global___AfterReferMessage | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["after_refer", b"after_refer", "empty", b"empty", "not_enable_user_pay", b"not_enable_user_pay", "user_pay", b"user_pay"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["after_refer", b"after_refer", "empty", b"empty", "include_enum", b"include_enum", "not_enable_user_pay", b"not_enable_user_pay", "user_list_map", b"user_list_map", "user_map", b"user_map", "user_pay", b"user_pay"]) -> None: ...

global___NestedMessage = NestedMessage

class AfterReferMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UID_FIELD_NUMBER: builtins.int
    AGE_FIELD_NUMBER: builtins.int
    uid: builtins.str
    """p2p: {"miss_default": true, "example": "10086", "title": "UID", "description": "user union id"}"""
    age: builtins.int
    """p2p: {"example": 18, "title": "use age", "ge": 0}"""
    def __init__(
        self,
        *,
        uid: builtins.str = ...,
        age: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["age", b"age", "uid", b"uid"]) -> None: ...

global___AfterReferMessage = AfterReferMessage

class InvoiceItem(google.protobuf.message.Message):
    """Test self-referencing Messages
    from: https://github.com/so1n/protobuf_to_pydantic/issues/7#issuecomment-1490705932
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    name: builtins.str
    amount: builtins.int
    quantity: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InvoiceItem]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        amount: builtins.int = ...,
        quantity: builtins.int = ...,
        items: collections.abc.Iterable[global___InvoiceItem] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount", "items", b"items", "name", b"name", "quantity", b"quantity"]) -> None: ...

global___InvoiceItem = InvoiceItem

class EmptyMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___EmptyMessage = EmptyMessage

class OptionalMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class IntMapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.int
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    AGE_FIELD_NUMBER: builtins.int
    ITEM_FIELD_NUMBER: builtins.int
    STR_LIST_FIELD_NUMBER: builtins.int
    INT_MAP_FIELD_NUMBER: builtins.int
    DEFAULT_TEMPLATE_TEST_FIELD_NUMBER: builtins.int
    x: builtins.str
    y: builtins.int
    """p2p: {"example": 18, "title": "use age", "ge": 0}"""
    name: builtins.str
    age: builtins.int
    @property
    def item(self) -> global___InvoiceItem: ...
    @property
    def str_list(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def int_map(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.int]: ...
    default_template_test: builtins.float
    """p2p: {"default_template": "p2p@timestamp|10"}"""
    def __init__(
        self,
        *,
        x: builtins.str = ...,
        y: builtins.int = ...,
        name: builtins.str | None = ...,
        age: builtins.int | None = ...,
        item: global___InvoiceItem | None = ...,
        str_list: collections.abc.Iterable[builtins.str] | None = ...,
        int_map: collections.abc.Mapping[builtins.str, builtins.int] | None = ...,
        default_template_test: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_age", b"_age", "_item", b"_item", "_name", b"_name", "a", b"a", "age", b"age", "item", b"item", "name", b"name", "x", b"x", "y", b"y"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_age", b"_age", "_item", b"_item", "_name", b"_name", "a", b"a", "age", b"age", "default_template_test", b"default_template_test", "int_map", b"int_map", "item", b"item", "name", b"name", "str_list", b"str_list", "x", b"x", "y", b"y"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_age", b"_age"]) -> typing_extensions.Literal["age"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_item", b"_item"]) -> typing_extensions.Literal["item"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_name", b"_name"]) -> typing_extensions.Literal["name"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["a", b"a"]) -> typing_extensions.Literal["x", "y"] | None: ...

global___OptionalMessage = OptionalMessage
