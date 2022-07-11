# protobuf_to_pydantic
Convert the `Python` Message object generated by the Protobuf file to a `pydantic.BaseModel` object with parameter validation.

> NOTE: Only support proto3

# 1.Installation
```bash
pip install protobuf_to_pydantic
```

# 2.Use
## 2.1.Transform objects at runtime
`protobuf_to_pydantic` can generate the corresponding `pydantic.BaseModel` object from the `Message` object at runtime.

For example, the `UserMessage` in the following Protobuf file:
```protobuf
syntax = "proto3";
package user;

enum SexType {
  man = 0;
  women = 1;
}

message UserMessage {
  string uid=1;
  int32 age=2;
  float height=3;
  SexType sex=4;
  bool is_adult=5;
  string user_name=6;
}
```
`protobuf_to_pydantic` can read the generated Message object at runtime and convert it to the corresponding `pydantic.BaseModel` object:
```Python
from typing import Type
from protobuf_to_pydantic import msg_to_pydantic_model
from pydantic import BaseModel

# import protobuf gen python obj
from example.python_example_proto_code.example_proto.demo import demo_pb2


UserModel: Type[BaseModel] = msg_to_pydantic_model(demo_pb2.UserMessage)
print(
    {
        k: v.field_info
        for k, v in UserModel.__fields__.items()
    }
)

# output
# {
#   'uid': FieldInfo(default='', extra={}),
#   'age': FieldInfo(default=0, extra={}),
#   'height': FieldInfo(default=0.0, extra={}),
#   'sex': FieldInfo(default=0, extra={}),
#   'is_adult': FieldInfo(default=False, extra={}),
#   'user_name': FieldInfo(default='', extra={})
#  }
```
## 2.2.PARAMETER VERIFICATION
The `Message` object generated according to the protobuf file only carries a small amount of information.
There is not enough information to make the generated `pydantic.BaseModel` have more detailed parameter verification functions, and some additional ways are needed to improve the data of the `Message` object.

At present, `protobuf_to_pydantic` supports multiple ways to obtain other information of Message, so that the generated `pydantic.BaseModel` object has the function of parameter verification.

### 2.2.1.TEXT COMMENT
Users can write comments that meet the requirements of `protobuf_to_pydantic` for each field in the protobuf file to provide parameter verification information for `protobuf_to_pydantic`, such as the following example
```protobuf
syntax = "proto3";
package user;

enum SexType {
  man = 0;
  women = 1;
}

// user info
message UserMessage {
  // p2p: {"miss_default": true, "example": "10086"}
  // p2p: {"title": "UID"}
  string uid=1; // p2p: {"description": "user union id"}
  // p2p: {"example": 18, "title": "use age", "ge": 0}
  int32 age=2;
  // p2p: {"ge": 0, "le": 2.5}
  float height=3;
  SexType sex=4;
  bool is_adult=5;
  // p2p: {"description": "user name"}
  // p2p: {"default": "", "min_length": 1, "max_length": "10", "example": "so1n"}
  string user_name=6;
}
```
In this example, every comment that can be used by `protobuf_to_pydantic` starts with `p2p:` and is followed by a full Json string. If you are familiar with the usage of `pydantic`, you can find This Json string contains the verification information of the corresponding field,
For example, the uid in `User Message` comes with the following 4 pieces of information:
- miss_default: Indicates that the generated field does not have a default value
- example: An example value representing the generated field is 10086
- title: Indicates that the name of the field is UID
- description: The documentation that represents the field is described as `user union id`

> Note:
>   - 1.Currently only supports single-line comments and comments must be a complete Json data (no line breaks)。
>   - 2.multi line comments are not supported。

When these annotations are written, `protobuf_to_pydantic` will bring the corresponding information for each field when converting the Message into the corresponding `Pydantic.BaseModel` object, as follows:
```python
from typing import Type
from protobuf_to_pydantic import msg_to_pydantic_model
from pydantic import BaseModel

# import protobuf gen python obj
from example.python_example_proto_code.example_proto.demo import demo_pb2

UserModel: Type[BaseModel] = msg_to_pydantic_model(demo_pb2.UserMessage, parse_msg_desc_method=demo_pb2)
print(
    {
        k: v.field_info
        for k, v in UserModel.__fields__.items()
    }
)
# output
# {
#   'uid': FieldInfo(default=PydanticUndefined, title='UID', description='user union id', extra={'example': '10086'}),
#   'age': FieldInfo(default=0, title='use age', ge=0, extra={'example': 18}),
#   'height': FieldInfo(default=0.0, ge=0, le=2, extra={}),
#   'sex': FieldInfo(default=0, extra={}),
#   'is_adult': FieldInfo(default=False, extra={}),
#   'user_name': FieldInfo(default='', description='user name', min_length=1, max_length=10, extra={'example': 'so1n'})
# }
```

#### 2.2.1.1.By pyi file
由于`Python.grpc_tools`把protobuf文件转为`Python`代码时并不会把Message的注释带到生成的`Python`代码中，所以上面的示例会把Message对象所属的模块传入`parse_msg_desc_method`中，
使得`protobuf_to_pydantic`可以通过读取Message对应的pyi文件的注释来获取Message对象的附加信息。

Since `Python.grpc_tools` converts the protobuf file to `Python` code, it does not bring the message's comments to the generated `Python` code,
so the above example will pass the module to which the Message object belongs to `parse_msg_desc_method` ,
so that `protobuf_to_pydantic` can obtain additional information of the Message object by reading the comments of the pyi file corresponding to the Message.

> Note: This function requires the [mypy-protobuf](https:github.comnipunn 1313 mypy-protobuf) plugin when generating the corresponding `Python` code from the Protobuf file, and the specified output path of the pyi file is the same as the generated `Python` code path to take effect when

#### 2.2.1.1.By Protobuf file

> NOTE: Need to install lark library in advance

If the original Protobuf file that generates the Message exists in the project, you can set the value of `parse_msg_desc_method` to the root directory path specified when the Message is generated.
In this way, `protobuf_to_pydantic` can obtain the protobuf file path of the Message object through the path specified when Protobuf generates the corresponding `Python` object, and then obtain the accompanying information of the Message by parsing the comments of the protobuf file.

For example, the project structure of `protobuf to pydantic` is as follows:
```bash
./protobuf_to_pydantic/
├── example/
│ ├── python_example_proto_code/
│ └── example_proto/
├── protobuf_to_pydantic/
└── /
```
其中protobuf文件存放在`example/example_proto`文件中，然后在`example`目录下通过如下命令生成protobuf对应的`Python`代码文件:
The protobuf file is stored in the `example/example_proto` file, and then the `Python` code file corresponding to protobuf is generated by the following command in the `example` directory:
```bash
cd example

python -m grpc_tools.protoc
  --python_out=./python_example_proto_code \
  --grpc_python_out=./python_example_proto_code \
  -I. \
```
Then the path that needs to be filled in at this time is`./protobuf_to_pydantic/example`。
```python
from typing import Type
from protobuf_to_pydantic import msg_to_pydantic_model
from pydantic import BaseModel

# import protobuf gen python obj
from example.python_example_proto_code.example_proto.demo import demo_pb2

UserModel: Type[BaseModel] = msg_to_pydantic_model(
    demo_pb2.UserMessage, parse_msg_desc_method="./protobuf_to_pydantic/example"
)
print(
    {
        k: v.field_info
        for k, v in UserModel.__fields__.items()
    }
)
# output
# {
#   'uid': FieldInfo(default=PydanticUndefined, title='UID', description='user union id', extra={'example': '10086'}),
#   'age': FieldInfo(default=0, title='use age', ge=0, extra={'example': 18}),
#   'height': FieldInfo(default=0.0, ge=0, le=2, extra={}),
#   'sex': FieldInfo(default=0, extra={}),
#   'is_adult': FieldInfo(default=False, extra={}),
#   'user_name': FieldInfo(default='', description='user name', min_length=1, max_length=10, extra={'example': 'so1n'})
# }
```

### 2.2.2.Protobuf Field Option(PGV)

> Note in development...

This is the most recommended way, which refers to the [protoc-gen-validate](https://github.com/envoyproxy/protoc-gen-validate) project, and most Protobuf file APIs refer to [protoc-gen-validate](https:github. comenvoyproxyprotoc-gen-validate) project

### 2.2.3.Other parameter support
In addition to the parameters of `FieldInfo`, `protobuf_to_pydantic` also supports the following parameters:
- miss_default：By default, the default values generated for each field in the `pydantic.BaseModel` object are the same as the default values for each field in the Message. However, you can cancel the default value setting by setting `miss_default` to `true`. It should be noted that in the case of setting `miss_default` to `true`, the `default` parameter will be invalid.
- enable: By default, `pydantic.BaseModel` will convert every field in the Message. If some fields do not want to be converted, you can set `enable` to `false`
- const: Specifies the value of the field's constant. Note: The const of `pydantic.BaseModel` only supports bool variables. When `const` is `True`, the accepted value can only be the value set by `default`, and the default value carried by the Message generated by protobuf corresponds to A null value of type does not match `pydantic.BaseModel`, so `protobuf)to_pydantic` makes some changes to the input of this value.
- type: Expand the current type, such as the following bank card number:
  ```protobuf
  message UserPayMessage {
    string bank_number=1; // p2p: {"type": "p2p@import|PaymentCardNumber|pydantic.types"}
  }
  ```

> Note See the parameters supported by `FieldInfo`:https://pydantic-docs.helpmanual.io/usage/types/#constrained-types

### 2.2.4.Template
In some cases, the value we fill in is a method or function of a library, such as the value of the `type` parameter and the `default factory` parameter, but Json does not support it. In this case, template parameters can be used。
Currently `protobuf to pydantic` supports two template parameters, the first one is `p 2 p@import`, the usage is as follows：
```protobuf
  message UserPayMessage {
    string bank_number=1; // p2p: {"type": "p2p@import|PaymentCardNumber|pydantic.types"}
  }
```
The comments here use the syntax of the `{p2p method}|{class to be imported or:A}|{class module:B}` format, where the method `p2p@import` at the beginning indicates that this needs to be passed ` from B import A` introduces an object，
By commenting, `protobuf to pydantic` will convert the corresponding Message to the following `pydantic.Base Model`:
```python
from pydantic import BaseModel
from pydantic.fields import FieldInfo
# p2p@import|PaymentCardNumber|pydantic.types
from pydantic.types import PaymentCardNumber

class UserPayMessage(BaseModel):
    bank_number: PaymentCardNumber = FieldInfo(default="", extra={})
```

The second method is `p2p@local`, which uses the syntax of `{p2p method}|{local variable to be used}` format, as follows：
```protobuf
message UserPayMessage {
  google.protobuf.Timestamp exp=1; // p2p: {"default_factory": "p2p@local|exp_time"}
}
```
Then register the corresponding value through the parameter `local_dict` when calling the `msg_to_pydantic_model` method, as follows：
```Python
def exp_time() -> float:
  return time.time()

msg_to_pydantic_model(
    demo_pb2.NestedMessage,
    parse_msg_desc_method="/home/so1n/github/protobuf_to_pydantic/example",
    local_dict={"exp_time": exp_time},  # <----
)
```
In this way, `protobuf to pydantic` can generate a `pydantic.Base Model` that meets the requirements：
```python
from pydantic import BaseModel
from pydantic.fields import FieldInfo

from example.simple_gen_code import exp_time

class UserPayMessage(BaseModel):
    exp: str = FieldInfo(default_factory=exp_time, extra={})
```

> Note: See the sample code for specific invocation and generation methods.

## 2.3.Generate the corresponding Python code
In addition to generating corresponding `pydantic.BaseModel` objects at runtime, `protobuf_to_pydantic` supports converting runtime `pydantic.BaseModel` objects to `Python` code literals (only for `pydantic.BaseModel` object).

Among them, `protobuf_to_pydantic.pydantic_model_to_py_code` is used to generate code text, `protobuf_to_pydantic.pydantic_model_to_py_file` is used to generate code file, the example of `protobuf_to_pydantic.pydantic_model_to_py_file` is as follows :
```Python
from protobuf_to_pydantic import msg_to_pydantic_model, pydantic_model_to_py_file

# import protobuf gen python obj
from example.python_example_proto_code.example_proto.demo import demo_pb2

# gen code: url: https://github.com/so1n/protobuf_to_pydantic/blob/master/example/demo_gen_code.py
pydantic_model_to_py_file(
    "./demo_gen_code.py",
    msg_to_pydantic_model(demo_pb2.NestedMessage),
)

# gen code: url: https://github.com/so1n/protobuf_to_pydantic/blob/master/example/demo_gen_code_by_pyi.py
pydantic_model_to_py_file(
    "./demo_gen_code_by_pyi.py",
    msg_to_pydantic_model(demo_pb2.NestedMessage, parse_msg_desc_method=demo_pb2),
)

# gen code: url: https://github.com/so1n/protobuf_to_pydantic/blob/master/example/demo_gen_code_by_protobuf_field.py
pydantic_model_to_py_file(
    "./demo_gen_code_by_protobuf_field.py",
    msg_to_pydantic_model(
        demo_pb2.NestedMessage, parse_msg_desc_method="/home/so1n/github/protobuf_to_pydantic/example"
    ),
)
```
The specific generated code can be viewed through the corresponding url. It should be noted that if `protobuf_to_pydantic` checks that the current environment has `isort` and `autoflake` installed, the code will be formatted by them by default.