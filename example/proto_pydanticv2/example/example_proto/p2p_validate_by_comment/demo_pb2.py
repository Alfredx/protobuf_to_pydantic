# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example/example_proto/p2p_validate_by_comment/demo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from example.proto_pydanticv2.example.example_proto.common import p2p_validate_pb2 as example_dot_example__proto_dot_common_dot_p2p__validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8example/example_proto/p2p_validate_by_comment/demo.proto\x12\x19p2p_validate_comment_test\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a/example/example_proto/common/p2p_validate.proto\"\xcc\x03\n\tFloatTest\x12\x12\n\nconst_test\x18\x01 \x01(\x02\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x02\x12\x12\n\nrange_test\x18\x03 \x01(\x02\x12\x0f\n\x07in_test\x18\x04 \x01(\x02\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x02\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x02\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x02\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x02\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x02\x12\x19\n\x11miss_default_test\x18\t \x01(\x02\x12\x15\n\rrequired_test\x18\x13 \x01(\x02\x12\x12\n\nalias_test\x18\n \x01(\x02\x12\x11\n\tdesc_test\x18\x0b \x01(\x02\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x02\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x02\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x02\x12\x12\n\nfield_test\x18\x0f \x01(\x02\x12\x11\n\ttype_test\x18\x10 \x01(\x02\x12\x12\n\ntitle_test\x18\x11 \x01(\x02\x12\x12\n\nextra_test\x18\x12 \x01(\x02\"\xcd\x03\n\nDoubleTest\x12\x12\n\nconst_test\x18\x01 \x01(\x01\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x01\x12\x12\n\nrange_test\x18\x03 \x01(\x01\x12\x0f\n\x07in_test\x18\x04 \x01(\x01\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x01\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x01\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x01\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x01\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x01\x12\x19\n\x11miss_default_test\x18\t \x01(\x01\x12\x15\n\rrequired_test\x18\x13 \x01(\x01\x12\x12\n\nalias_test\x18\n \x01(\x01\x12\x11\n\tdesc_test\x18\x0b \x01(\x01\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x01\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x01\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x01\x12\x12\n\nfield_test\x18\x0f \x01(\x01\x12\x11\n\ttype_test\x18\x10 \x01(\x01\x12\x12\n\ntitle_test\x18\x11 \x01(\x01\x12\x12\n\nextra_test\x18\x12 \x01(\x01\"\xcc\x03\n\tInt32Test\x12\x12\n\nconst_test\x18\x01 \x01(\x05\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x05\x12\x12\n\nrange_test\x18\x03 \x01(\x05\x12\x0f\n\x07in_test\x18\x04 \x01(\x05\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x05\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x05\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x05\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x05\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x05\x12\x19\n\x11miss_default_test\x18\t \x01(\x05\x12\x15\n\rrequired_test\x18\x13 \x01(\x05\x12\x12\n\nalias_test\x18\n \x01(\x05\x12\x11\n\tdesc_test\x18\x0b \x01(\x05\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x05\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x05\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x05\x12\x12\n\nfield_test\x18\x0f \x01(\x05\x12\x11\n\ttype_test\x18\x10 \x01(\x05\x12\x12\n\ntitle_test\x18\x11 \x01(\x05\x12\x12\n\nextra_test\x18\x12 \x01(\x05\"\xcc\x03\n\tInt64Test\x12\x12\n\nconst_test\x18\x01 \x01(\x03\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x03\x12\x12\n\nrange_test\x18\x03 \x01(\x03\x12\x0f\n\x07in_test\x18\x04 \x01(\x03\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x03\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x03\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x03\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x03\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x03\x12\x19\n\x11miss_default_test\x18\t \x01(\x03\x12\x15\n\rrequired_test\x18\x13 \x01(\x03\x12\x12\n\nalias_test\x18\n \x01(\x03\x12\x11\n\tdesc_test\x18\x0b \x01(\x03\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x03\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x03\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x03\x12\x12\n\nfield_test\x18\x0f \x01(\x03\x12\x11\n\ttype_test\x18\x10 \x01(\x03\x12\x12\n\ntitle_test\x18\x11 \x01(\x03\x12\x12\n\nextra_test\x18\x12 \x01(\x03\"\xcd\x03\n\nUint32Test\x12\x12\n\nconst_test\x18\x01 \x01(\r\x12\x14\n\x0crange_e_test\x18\x02 \x01(\r\x12\x12\n\nrange_test\x18\x03 \x01(\r\x12\x0f\n\x07in_test\x18\x04 \x01(\r\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\r\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\r\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\r\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\r\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\r\x12\x19\n\x11miss_default_test\x18\t \x01(\r\x12\x15\n\rrequired_test\x18\x13 \x01(\r\x12\x12\n\nalias_test\x18\n \x01(\r\x12\x11\n\tdesc_test\x18\x0b \x01(\r\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\r\x12\x14\n\x0c\x65xample_test\x18\r \x01(\r\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\r\x12\x12\n\nfield_test\x18\x0f \x01(\r\x12\x11\n\ttype_test\x18\x10 \x01(\r\x12\x12\n\ntitle_test\x18\x11 \x01(\r\x12\x12\n\nextra_test\x18\x12 \x01(\r\"\xcd\x03\n\nSint32Test\x12\x12\n\nconst_test\x18\x01 \x01(\x11\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x11\x12\x12\n\nrange_test\x18\x03 \x01(\x11\x12\x0f\n\x07in_test\x18\x04 \x01(\x11\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x11\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x11\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x11\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x11\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x11\x12\x19\n\x11miss_default_test\x18\t \x01(\x11\x12\x15\n\rrequired_test\x18\x13 \x01(\x11\x12\x12\n\nalias_test\x18\n \x01(\x11\x12\x11\n\tdesc_test\x18\x0b \x01(\x11\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x11\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x11\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x11\x12\x12\n\nfield_test\x18\x0f \x01(\x11\x12\x11\n\ttype_test\x18\x10 \x01(\x11\x12\x12\n\ntitle_test\x18\x11 \x01(\x11\x12\x12\n\nextra_test\x18\x12 \x01(\x11\"\xcd\x03\n\nUint64Test\x12\x12\n\nconst_test\x18\x01 \x01(\x04\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x04\x12\x12\n\nrange_test\x18\x03 \x01(\x04\x12\x0f\n\x07in_test\x18\x04 \x01(\x04\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x04\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x04\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x04\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x04\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x04\x12\x19\n\x11miss_default_test\x18\t \x01(\x04\x12\x15\n\rrequired_test\x18\x13 \x01(\x04\x12\x12\n\nalias_test\x18\n \x01(\x04\x12\x11\n\tdesc_test\x18\x0b \x01(\x04\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x04\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x04\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x04\x12\x12\n\nfield_test\x18\x0f \x01(\x04\x12\x11\n\ttype_test\x18\x10 \x01(\x04\x12\x12\n\ntitle_test\x18\x11 \x01(\x04\x12\x12\n\nextra_test\x18\x12 \x01(\x04\"\xcd\x03\n\nSint64Test\x12\x12\n\nconst_test\x18\x01 \x01(\x12\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x12\x12\x12\n\nrange_test\x18\x03 \x01(\x12\x12\x0f\n\x07in_test\x18\x04 \x01(\x12\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x12\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x12\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x12\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x12\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x12\x12\x19\n\x11miss_default_test\x18\t \x01(\x12\x12\x15\n\rrequired_test\x18\x13 \x01(\x12\x12\x12\n\nalias_test\x18\n \x01(\x12\x12\x11\n\tdesc_test\x18\x0b \x01(\x12\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x12\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x12\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x12\x12\x12\n\nfield_test\x18\x0f \x01(\x12\x12\x11\n\ttype_test\x18\x10 \x01(\x12\x12\x12\n\ntitle_test\x18\x11 \x01(\x12\x12\x12\n\nextra_test\x18\x12 \x01(\x12\"\xce\x03\n\x0b\x46ixed32Test\x12\x12\n\nconst_test\x18\x01 \x01(\x07\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x07\x12\x12\n\nrange_test\x18\x03 \x01(\x07\x12\x0f\n\x07in_test\x18\x04 \x01(\x07\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x07\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x07\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x07\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x07\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x07\x12\x19\n\x11miss_default_test\x18\t \x01(\x07\x12\x15\n\rrequired_test\x18\x13 \x01(\x07\x12\x12\n\nalias_test\x18\n \x01(\x07\x12\x11\n\tdesc_test\x18\x0b \x01(\x07\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x07\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x07\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x07\x12\x12\n\nfield_test\x18\x0f \x01(\x07\x12\x11\n\ttype_test\x18\x10 \x01(\x07\x12\x12\n\ntitle_test\x18\x11 \x01(\x07\x12\x12\n\nextra_test\x18\x12 \x01(\x07\"\xce\x03\n\x0b\x46ixed64Test\x12\x12\n\nconst_test\x18\x01 \x01(\x06\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x06\x12\x12\n\nrange_test\x18\x03 \x01(\x06\x12\x0f\n\x07in_test\x18\x04 \x01(\x06\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x06\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x06\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x06\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x06\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x06\x12\x19\n\x11miss_default_test\x18\t \x01(\x06\x12\x15\n\rrequired_test\x18\x13 \x01(\x06\x12\x12\n\nalias_test\x18\n \x01(\x06\x12\x11\n\tdesc_test\x18\x0b \x01(\x06\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x06\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x06\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x06\x12\x12\n\nfield_test\x18\x0f \x01(\x06\x12\x11\n\ttype_test\x18\x10 \x01(\x06\x12\x12\n\ntitle_test\x18\x11 \x01(\x06\x12\x12\n\nextra_test\x18\x12 \x01(\x06\"\xcf\x03\n\x0cSfixed32Test\x12\x12\n\nconst_test\x18\x01 \x01(\x0f\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x0f\x12\x12\n\nrange_test\x18\x03 \x01(\x0f\x12\x0f\n\x07in_test\x18\x04 \x01(\x0f\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x0f\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x0f\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x0f\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x0f\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x0f\x12\x19\n\x11miss_default_test\x18\t \x01(\x0f\x12\x15\n\rrequired_test\x18\x13 \x01(\x0f\x12\x12\n\nalias_test\x18\n \x01(\x0f\x12\x11\n\tdesc_test\x18\x0b \x01(\x0f\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x0f\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x0f\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x0f\x12\x12\n\nfield_test\x18\x0f \x01(\x0f\x12\x11\n\ttype_test\x18\x10 \x01(\x0f\x12\x12\n\ntitle_test\x18\x11 \x01(\x0f\x12\x12\n\nextra_test\x18\x12 \x01(\x0f\"\xcf\x03\n\x0cSfixed64Test\x12\x12\n\nconst_test\x18\x01 \x01(\x10\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x10\x12\x12\n\nrange_test\x18\x03 \x01(\x10\x12\x0f\n\x07in_test\x18\x04 \x01(\x10\x12\x13\n\x0bnot_in_test\x18\x05 \x01(\x10\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x06 \x01(\x10\x12\x1d\n\x15\x64\x65\x66\x61ult_template_test\x18\x14 \x01(\x10\x12\x17\n\x0fnot_enable_test\x18\x07 \x01(\x10\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x08 \x01(\x10\x12\x19\n\x11miss_default_test\x18\t \x01(\x10\x12\x15\n\rrequired_test\x18\x13 \x01(\x10\x12\x12\n\nalias_test\x18\n \x01(\x10\x12\x11\n\tdesc_test\x18\x0b \x01(\x10\x12\x18\n\x10multiple_of_test\x18\x0c \x01(\x10\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x10\x12\x17\n\x0f\x65xample_factory\x18\x0e \x01(\x10\x12\x12\n\nfield_test\x18\x0f \x01(\x10\x12\x11\n\ttype_test\x18\x10 \x01(\x10\x12\x12\n\ntitle_test\x18\x11 \x01(\x10\x12\x12\n\nextra_test\x18\x12 \x01(\x10\"\x8a\x02\n\x08\x42oolTest\x12\x13\n\x0b\x62ool_1_test\x18\x01 \x01(\x08\x12\x13\n\x0b\x62ool_2_test\x18\x02 \x01(\x08\x12\x13\n\x0b\x65nable_test\x18\x03 \x01(\x08\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x04 \x01(\x08\x12\x19\n\x11miss_default_test\x18\x05 \x01(\x08\x12\x15\n\rrequired_test\x18\x13 \x01(\x08\x12\x12\n\nalias_test\x18\n \x01(\x08\x12\x11\n\tdesc_test\x18\x0b \x01(\x08\x12\x14\n\x0c\x65xample_test\x18\r \x01(\x08\x12\x12\n\nfield_test\x18\x0f \x01(\x08\x12\x12\n\ntitle_test\x18\x11 \x01(\x08\x12\x12\n\nextra_test\x18\x12 \x01(\x08\"\xd8\x05\n\nStringTest\x12\x12\n\nconst_test\x18\x01 \x01(\t\x12\x10\n\x08len_test\x18\x02 \x01(\t\x12\x18\n\x10s_range_len_test\x18\x03 \x01(\t\x12\x14\n\x0cpattern_test\x18\x05 \x01(\t\x12\x13\n\x0bprefix_test\x18\x06 \x01(\t\x12\x13\n\x0bsuffix_test\x18\x07 \x01(\t\x12\x15\n\rcontains_test\x18\x08 \x01(\t\x12\x19\n\x11not_contains_test\x18\t \x01(\t\x12\x0f\n\x07in_test\x18\n \x01(\t\x12\x13\n\x0bnot_in_test\x18\x0b \x01(\t\x12\x12\n\nemail_test\x18\x0c \x01(\t\x12\x15\n\rhostname_test\x18\r \x01(\t\x12\x0f\n\x07ip_test\x18\x0e \x01(\t\x12\x11\n\tipv4_test\x18\x0f \x01(\t\x12\x11\n\tipv6_test\x18\x10 \x01(\t\x12\x10\n\x08uri_test\x18\x11 \x01(\t\x12\x14\n\x0curi_ref_test\x18\x12 \x01(\t\x12\x14\n\x0c\x61\x64\x64ress_test\x18\x13 \x01(\t\x12\x11\n\tuuid_test\x18\x14 \x01(\t\x12\x1a\n\x12pydantic_type_test\x18\x15 \x01(\t\x12\x13\n\x0b\x65nable_test\x18\x16 \x01(\t\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x17 \x01(\t\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x18 \x01(\t\x12\x19\n\x11miss_default_test\x18\x19 \x01(\t\x12\x15\n\rrequired_test\x18\" \x01(\t\x12\x12\n\nalias_test\x18\x1a \x01(\t\x12\x11\n\tdesc_test\x18\x1b \x01(\t\x12\x14\n\x0c\x65xample_test\x18\x1c \x01(\t\x12\x1c\n\x14\x65xample_factory_test\x18\x1d \x01(\t\x12\x12\n\nfield_test\x18\x1e \x01(\t\x12\x12\n\ntitle_test\x18\x1f \x01(\t\x12\x11\n\ttype_test\x18  \x01(\t\x12\x12\n\nextra_test\x18! \x01(\t\"\xc3\x03\n\tBytesTest\x12\x12\n\nconst_test\x18\x01 \x01(\x0c\x12\x16\n\x0erange_len_test\x18\x03 \x01(\x0c\x12\x13\n\x0bprefix_test\x18\x05 \x01(\x0c\x12\x13\n\x0bsuffix_test\x18\x06 \x01(\x0c\x12\x15\n\rcontains_test\x18\x07 \x01(\x0c\x12\x0f\n\x07in_test\x18\x08 \x01(\x0c\x12\x13\n\x0bnot_in_test\x18\t \x01(\x0c\x12\x13\n\x0b\x65nable_test\x18\x16 \x01(\x0c\x12\x14\n\x0c\x64\x65\x66\x61ult_test\x18\x17 \x01(\x0c\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x18 \x01(\x0c\x12\x19\n\x11miss_default_test\x18\x19 \x01(\x0c\x12\x15\n\rrequired_test\x18\" \x01(\x0c\x12\x12\n\nalias_test\x18\x1a \x01(\x0c\x12\x11\n\tdesc_test\x18\x1b \x01(\x0c\x12\x14\n\x0c\x65xample_test\x18\x1c \x01(\x0c\x12\x1c\n\x14\x65xample_factory_test\x18\x1d \x01(\x0c\x12\x12\n\nfield_test\x18\x1e \x01(\x0c\x12\x12\n\ntitle_test\x18\x1f \x01(\x0c\x12\x11\n\ttype_test\x18  \x01(\x0c\x12\x12\n\nextra_test\x18! \x01(\x0c\"\xd4\x05\n\x08\x45numTest\x12\x34\n\nconst_test\x18\x01 \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x31\n\x07in_test\x18\x03 \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x35\n\x0bnot_in_test\x18\x04 \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x35\n\x0b\x65nable_test\x18\x16 \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x36\n\x0c\x64\x65\x66\x61ult_test\x18\x17 \x01(\x0e\x32 .p2p_validate_comment_test.State\x12;\n\x11miss_default_test\x18\x19 \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x37\n\rrequired_test\x18\" \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x34\n\nalias_test\x18\x1a \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x33\n\tdesc_test\x18\x1b \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x36\n\x0c\x65xample_test\x18\x1c \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x34\n\nfield_test\x18\x1e \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x34\n\ntitle_test\x18\x1f \x01(\x0e\x32 .p2p_validate_comment_test.State\x12\x34\n\nextra_test\x18! \x01(\x0e\x32 .p2p_validate_comment_test.State\"\x9a\x0f\n\x07MapTest\x12\x43\n\tpair_test\x18\x01 \x03(\x0b\x32\x30.p2p_validate_comment_test.MapTest.PairTestEntry\x12\x43\n\tkeys_test\x18\x03 \x03(\x0b\x32\x30.p2p_validate_comment_test.MapTest.KeysTestEntry\x12G\n\x0bvalues_test\x18\x04 \x03(\x0b\x32\x32.p2p_validate_comment_test.MapTest.ValuesTestEntry\x12P\n\x10keys_values_test\x18\x05 \x03(\x0b\x32\x36.p2p_validate_comment_test.MapTest.KeysValuesTestEntry\x12G\n\x0b\x65nable_test\x18\x06 \x03(\x0b\x32\x32.p2p_validate_comment_test.MapTest.EnableTestEntry\x12X\n\x14\x64\x65\x66\x61ult_factory_test\x18\x18 \x03(\x0b\x32:.p2p_validate_comment_test.MapTest.DefaultFactoryTestEntry\x12R\n\x11miss_default_test\x18\x19 \x03(\x0b\x32\x37.p2p_validate_comment_test.MapTest.MissDefaultTestEntry\x12K\n\rrequired_test\x18\" \x03(\x0b\x32\x34.p2p_validate_comment_test.MapTest.RequiredTestEntry\x12\x45\n\nalias_test\x18\x1a \x03(\x0b\x32\x31.p2p_validate_comment_test.MapTest.AliasTestEntry\x12\x43\n\tdesc_test\x18\x1b \x03(\x0b\x32\x30.p2p_validate_comment_test.MapTest.DescTestEntry\x12X\n\x14\x65xample_factory_test\x18\x1d \x03(\x0b\x32:.p2p_validate_comment_test.MapTest.ExampleFactoryTestEntry\x12\x45\n\nfield_test\x18\x1e \x03(\x0b\x32\x31.p2p_validate_comment_test.MapTest.FieldTestEntry\x12\x45\n\ntitle_test\x18\x1f \x03(\x0b\x32\x31.p2p_validate_comment_test.MapTest.TitleTestEntry\x12\x43\n\ttype_test\x18  \x03(\x0b\x32\x30.p2p_validate_comment_test.MapTest.TypeTestEntry\x12\x45\n\nextra_test\x18! \x03(\x0b\x32\x31.p2p_validate_comment_test.MapTest.ExtraTestEntry\x1a/\n\rPairTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a/\n\rKeysTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x31\n\x0fValuesTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1aQ\n\x13KeysValuesTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\x02\x38\x01\x1a\x31\n\x0f\x45nableTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17\x44\x65\x66\x61ultFactoryTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x36\n\x14MissDefaultTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x33\n\x11RequiredTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x30\n\x0e\x41liasTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a/\n\rDescTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17\x45xampleFactoryTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x30\n\x0e\x46ieldTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x30\n\x0eTitleTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a/\n\rTypeTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x30\n\x0e\x45xtraTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"K\n\x0bMessageTest\x12\x11\n\tskip_test\x18\x01 \x01(\t\x12\x15\n\rrequired_test\x18\x02 \x01(\t\x12\x12\n\nextra_test\x18! \x01(\t\"\x8c\x04\n\x0cRepeatedTest\x12\x12\n\nrange_test\x18\x01 \x03(\t\x12\x13\n\x0bunique_test\x18\x02 \x03(\t\x12\x19\n\x11items_string_test\x18\x03 \x03(\t\x12\x19\n\x11items_double_test\x18\x04 \x03(\x01\x12\x18\n\x10items_int32_test\x18\x05 \x03(\x05\x12\x38\n\x14items_timestamp_test\x18\x06 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x13items_duration_test\x18\x07 \x03(\x0b\x32\x19.google.protobuf.Duration\x12\x18\n\x10items_bytes_test\x18\x08 \x03(\x0c\x12\x13\n\x0b\x65nable_test\x18\t \x03(\t\x12\x1c\n\x14\x64\x65\x66\x61ult_factory_test\x18\x18 \x03(\t\x12\x19\n\x11miss_default_test\x18\x19 \x03(\t\x12\x15\n\rrequired_test\x18\" \x03(\t\x12\x12\n\nalias_test\x18\x1a \x03(\t\x12\x11\n\tdesc_test\x18\x1b \x03(\t\x12\x1c\n\x14\x65xample_factory_test\x18\x1d \x03(\t\x12\x12\n\nfield_test\x18\x1e \x03(\t\x12\x12\n\ntitle_test\x18\x1f \x03(\t\x12\x11\n\ttype_test\x18  \x03(\t\x12\x12\n\nextra_test\x18! \x03(\t\"\xf5\x04\n\x07\x41nyTest\x12+\n\rrequired_test\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12)\n\x0bnot_in_test\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12%\n\x07in_test\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12)\n\x0b\x65nable_test\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\x12*\n\x0c\x64\x65\x66\x61ult_test\x18\x17 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x32\n\x14\x64\x65\x66\x61ult_factory_test\x18\x18 \x01(\x0b\x32\x14.google.protobuf.Any\x12/\n\x11miss_default_test\x18\x19 \x01(\x0b\x32\x14.google.protobuf.Any\x12(\n\nalias_test\x18\x1a \x01(\x0b\x32\x14.google.protobuf.Any\x12\'\n\tdesc_test\x18\x1b \x01(\x0b\x32\x14.google.protobuf.Any\x12*\n\x0c\x65xample_test\x18\x1c \x01(\x0b\x32\x14.google.protobuf.Any\x12\x32\n\x14\x65xample_factory_test\x18\x1d \x01(\x0b\x32\x14.google.protobuf.Any\x12(\n\nfield_test\x18\x1e \x01(\x0b\x32\x14.google.protobuf.Any\x12(\n\ntitle_test\x18\x1f \x01(\x0b\x32\x14.google.protobuf.Any\x12(\n\nextra_test\x18! \x01(\x0b\x32\x14.google.protobuf.Any\"\xfd\x06\n\x0c\x44urationTest\x12-\n\nconst_test\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12-\n\nrange_test\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0crange_e_test\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12*\n\x07in_test\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12.\n\x0bnot_in_test\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12.\n\x0b\x65nable_test\x18\x16 \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0c\x64\x65\x66\x61ult_test\x18\x17 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\x14\x64\x65\x66\x61ult_factory_test\x18\x18 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x34\n\x11miss_default_test\x18\x19 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x30\n\rrequired_test\x18\" \x01(\x0b\x32\x19.google.protobuf.Duration\x12-\n\nalias_test\x18\x1a \x01(\x0b\x32\x19.google.protobuf.Duration\x12,\n\tdesc_test\x18\x1b \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0c\x65xample_test\x18\x1c \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\x14\x65xample_factory_test\x18\x1d \x01(\x0b\x32\x19.google.protobuf.Duration\x12-\n\nfield_test\x18\x1e \x01(\x0b\x32\x19.google.protobuf.Duration\x12-\n\ntitle_test\x18\x1f \x01(\x0b\x32\x19.google.protobuf.Duration\x12,\n\ttype_test\x18  \x01(\x0b\x32\x19.google.protobuf.Duration\x12-\n\nextra_test\x18! \x01(\x0b\x32\x19.google.protobuf.Duration\"\x81\x08\n\rTimestampTest\x12.\n\nconst_test\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nrange_test\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0crange_e_test\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0blt_now_test\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bgt_now_test\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bwithin_test\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16within_and_gt_now_test\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x65nable_test\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x64\x65\x66\x61ult_test\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14\x64\x65\x66\x61ult_factory_test\x18\x18 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11miss_default_test\x18\x19 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rrequired_test\x18\" \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nalias_test\x18\x1a \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tdesc_test\x18\x1b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x65xample_test\x18\x1c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14\x65xample_factory_test\x18\x1d \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nfield_test\x18\x1e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ntitle_test\x18\x1f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\ttype_test\x18  \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nextra_test\x18! \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"R\n\x12MessageIgnoredTest\x12\x12\n\nconst_test\x18\x01 \x01(\x05\x12\x14\n\x0crange_e_test\x18\x02 \x01(\x05\x12\x12\n\nrange_test\x18\x03 \x01(\x05\";\n\tOneOfTest\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x0b\n\x01x\x18\x02 \x01(\tH\x00\x12\x0b\n\x01y\x18\x03 \x01(\x05H\x00\x42\x04\n\x02id\">\n\x0cOneOfNotTest\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x0b\n\x01x\x18\x02 \x01(\tH\x00\x12\x0b\n\x01y\x18\x03 \x01(\x05H\x00\x42\x04\n\x02id\"\x92\x02\n\x11OneOfOptionalTest\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x0b\n\x01x\x18\x02 \x01(\tH\x00\x12\x0b\n\x01y\x18\x03 \x01(\x05H\x00\x12\x0b\n\x01z\x18\x04 \x01(\x08H\x00\x12\x11\n\x04name\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03\x61ge\x18\x06 \x01(\x05H\x02\x88\x01\x01\x12\x10\n\x08str_list\x18\x07 \x03(\t\x12I\n\x07int_map\x18\x08 \x03(\x0b\x32\x38.p2p_validate_comment_test.OneOfOptionalTest.IntMapEntry\x1a-\n\x0bIntMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x42\x04\n\x02idB\x07\n\x05_nameB\x06\n\x04_age\"\xd0\x06\n\rNestedMessage\x12Y\n\x12string_in_map_test\x18\x01 \x03(\x0b\x32=.p2p_validate_comment_test.NestedMessage.StringInMapTestEntry\x12S\n\x0fmap_in_map_test\x18\x02 \x03(\x0b\x32:.p2p_validate_comment_test.NestedMessage.MapInMapTestEntry\x12I\n\x08user_pay\x18\x03 \x01(\x0b\x32\x37.p2p_validate_comment_test.NestedMessage.UserPayMessage\x12]\n\x13not_enable_user_pay\x18\x04 \x01(\x0b\x32@.p2p_validate_comment_test.NestedMessage.NotEnableUserPayMessage\x12%\n\x05\x65mpty\x18\x05 \x01(\x0b\x32\x16.google.protobuf.Empty\x12\x41\n\x0b\x61\x66ter_refer\x18\x07 \x01(\x0b\x32,.p2p_validate_comment_test.AfterReferMessage\x1a\\\n\x0eUserPayMessage\x12\x13\n\x0b\x62\x61nk_number\x18\x01 \x01(\t\x12\'\n\x03\x65xp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x1a\x65\n\x17NotEnableUserPayMessage\x12\x13\n\x0b\x62\x61nk_number\x18\x01 \x01(\t\x12\'\n\x03\x65xp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x1a]\n\x14StringInMapTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.p2p_validate_comment_test.StringTest:\x02\x38\x01\x1aW\n\x11MapInMapTestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".p2p_validate_comment_test.MapTest:\x02\x38\x01\"-\n\x11\x41\x66terReferMessage\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05*.\n\x05State\x12\x0c\n\x08INACTIVE\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example.example_proto.p2p_validate_by_comment.demo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAPTEST_PAIRTESTENTRY._options = None
  _MAPTEST_PAIRTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_KEYSTESTENTRY._options = None
  _MAPTEST_KEYSTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_VALUESTESTENTRY._options = None
  _MAPTEST_VALUESTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_KEYSVALUESTESTENTRY._options = None
  _MAPTEST_KEYSVALUESTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_ENABLETESTENTRY._options = None
  _MAPTEST_ENABLETESTENTRY._serialized_options = b'8\001'
  _MAPTEST_DEFAULTFACTORYTESTENTRY._options = None
  _MAPTEST_DEFAULTFACTORYTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_MISSDEFAULTTESTENTRY._options = None
  _MAPTEST_MISSDEFAULTTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_REQUIREDTESTENTRY._options = None
  _MAPTEST_REQUIREDTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_ALIASTESTENTRY._options = None
  _MAPTEST_ALIASTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_DESCTESTENTRY._options = None
  _MAPTEST_DESCTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_EXAMPLEFACTORYTESTENTRY._options = None
  _MAPTEST_EXAMPLEFACTORYTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_FIELDTESTENTRY._options = None
  _MAPTEST_FIELDTESTENTRY._serialized_options = b'8\001'
  _MAPTEST_TITLETESTENTRY._options = None
  _MAPTEST_TITLETESTENTRY._serialized_options = b'8\001'
  _MAPTEST_TYPETESTENTRY._options = None
  _MAPTEST_TYPETESTENTRY._serialized_options = b'8\001'
  _MAPTEST_EXTRATESTENTRY._options = None
  _MAPTEST_EXTRATESTENTRY._serialized_options = b'8\001'
  _ONEOFOPTIONALTEST_INTMAPENTRY._options = None
  _ONEOFOPTIONALTEST_INTMAPENTRY._serialized_options = b'8\001'
  _NESTEDMESSAGE_STRINGINMAPTESTENTRY._options = None
  _NESTEDMESSAGE_STRINGINMAPTESTENTRY._serialized_options = b'8\001'
  _NESTEDMESSAGE_MAPINMAPTESTENTRY._options = None
  _NESTEDMESSAGE_MAPINMAPTESTENTRY._serialized_options = b'8\001'
  _STATE._serialized_start=14502
  _STATE._serialized_end=14548
  _FLOATTEST._serialized_start=258
  _FLOATTEST._serialized_end=718
  _DOUBLETEST._serialized_start=721
  _DOUBLETEST._serialized_end=1182
  _INT32TEST._serialized_start=1185
  _INT32TEST._serialized_end=1645
  _INT64TEST._serialized_start=1648
  _INT64TEST._serialized_end=2108
  _UINT32TEST._serialized_start=2111
  _UINT32TEST._serialized_end=2572
  _SINT32TEST._serialized_start=2575
  _SINT32TEST._serialized_end=3036
  _UINT64TEST._serialized_start=3039
  _UINT64TEST._serialized_end=3500
  _SINT64TEST._serialized_start=3503
  _SINT64TEST._serialized_end=3964
  _FIXED32TEST._serialized_start=3967
  _FIXED32TEST._serialized_end=4429
  _FIXED64TEST._serialized_start=4432
  _FIXED64TEST._serialized_end=4894
  _SFIXED32TEST._serialized_start=4897
  _SFIXED32TEST._serialized_end=5360
  _SFIXED64TEST._serialized_start=5363
  _SFIXED64TEST._serialized_end=5826
  _BOOLTEST._serialized_start=5829
  _BOOLTEST._serialized_end=6095
  _STRINGTEST._serialized_start=6098
  _STRINGTEST._serialized_end=6826
  _BYTESTEST._serialized_start=6829
  _BYTESTEST._serialized_end=7280
  _ENUMTEST._serialized_start=7283
  _ENUMTEST._serialized_end=8007
  _MAPTEST._serialized_start=8010
  _MAPTEST._serialized_end=9956
  _MAPTEST_PAIRTESTENTRY._serialized_start=9150
  _MAPTEST_PAIRTESTENTRY._serialized_end=9197
  _MAPTEST_KEYSTESTENTRY._serialized_start=9199
  _MAPTEST_KEYSTESTENTRY._serialized_end=9246
  _MAPTEST_VALUESTESTENTRY._serialized_start=9248
  _MAPTEST_VALUESTESTENTRY._serialized_end=9297
  _MAPTEST_KEYSVALUESTESTENTRY._serialized_start=9299
  _MAPTEST_KEYSVALUESTESTENTRY._serialized_end=9380
  _MAPTEST_ENABLETESTENTRY._serialized_start=9382
  _MAPTEST_ENABLETESTENTRY._serialized_end=9431
  _MAPTEST_DEFAULTFACTORYTESTENTRY._serialized_start=9433
  _MAPTEST_DEFAULTFACTORYTESTENTRY._serialized_end=9490
  _MAPTEST_MISSDEFAULTTESTENTRY._serialized_start=9492
  _MAPTEST_MISSDEFAULTTESTENTRY._serialized_end=9546
  _MAPTEST_REQUIREDTESTENTRY._serialized_start=9548
  _MAPTEST_REQUIREDTESTENTRY._serialized_end=9599
  _MAPTEST_ALIASTESTENTRY._serialized_start=9601
  _MAPTEST_ALIASTESTENTRY._serialized_end=9649
  _MAPTEST_DESCTESTENTRY._serialized_start=9651
  _MAPTEST_DESCTESTENTRY._serialized_end=9698
  _MAPTEST_EXAMPLEFACTORYTESTENTRY._serialized_start=9700
  _MAPTEST_EXAMPLEFACTORYTESTENTRY._serialized_end=9757
  _MAPTEST_FIELDTESTENTRY._serialized_start=9759
  _MAPTEST_FIELDTESTENTRY._serialized_end=9807
  _MAPTEST_TITLETESTENTRY._serialized_start=9809
  _MAPTEST_TITLETESTENTRY._serialized_end=9857
  _MAPTEST_TYPETESTENTRY._serialized_start=9859
  _MAPTEST_TYPETESTENTRY._serialized_end=9906
  _MAPTEST_EXTRATESTENTRY._serialized_start=9908
  _MAPTEST_EXTRATESTENTRY._serialized_end=9956
  _MESSAGETEST._serialized_start=9958
  _MESSAGETEST._serialized_end=10033
  _REPEATEDTEST._serialized_start=10036
  _REPEATEDTEST._serialized_end=10560
  _ANYTEST._serialized_start=10563
  _ANYTEST._serialized_end=11192
  _DURATIONTEST._serialized_start=11195
  _DURATIONTEST._serialized_end=12088
  _TIMESTAMPTEST._serialized_start=12091
  _TIMESTAMPTEST._serialized_end=13116
  _MESSAGEIGNOREDTEST._serialized_start=13118
  _MESSAGEIGNOREDTEST._serialized_end=13200
  _ONEOFTEST._serialized_start=13202
  _ONEOFTEST._serialized_end=13261
  _ONEOFNOTTEST._serialized_start=13263
  _ONEOFNOTTEST._serialized_end=13325
  _ONEOFOPTIONALTEST._serialized_start=13328
  _ONEOFOPTIONALTEST._serialized_end=13602
  _ONEOFOPTIONALTEST_INTMAPENTRY._serialized_start=13534
  _ONEOFOPTIONALTEST_INTMAPENTRY._serialized_end=13579
  _NESTEDMESSAGE._serialized_start=13605
  _NESTEDMESSAGE._serialized_end=14453
  _NESTEDMESSAGE_USERPAYMESSAGE._serialized_start=14074
  _NESTEDMESSAGE_USERPAYMESSAGE._serialized_end=14166
  _NESTEDMESSAGE_NOTENABLEUSERPAYMESSAGE._serialized_start=14168
  _NESTEDMESSAGE_NOTENABLEUSERPAYMESSAGE._serialized_end=14269
  _NESTEDMESSAGE_STRINGINMAPTESTENTRY._serialized_start=14271
  _NESTEDMESSAGE_STRINGINMAPTESTENTRY._serialized_end=14364
  _NESTEDMESSAGE_MAPINMAPTESTENTRY._serialized_start=14366
  _NESTEDMESSAGE_MAPINMAPTESTENTRY._serialized_end=14453
  _AFTERREFERMESSAGE._serialized_start=14455
  _AFTERREFERMESSAGE._serialized_end=14500
# @@protoc_insertion_point(module_scope)
