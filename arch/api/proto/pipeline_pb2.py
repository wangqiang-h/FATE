#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy.proto
import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pipeline.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=_b('B\rPipelineProto'),
  serialized_pb=_b('\n\x0epipeline.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"P\n\x08Pipeline\x12\x15\n\rinference_dsl\x18\x01 \x01(\x0c\x12\x11\n\ttrain_dsl\x18\x02 \x01(\x0c\x12\x1a\n\x12train_runtime_conf\x18\x03 \x01(\x0c\x42\x0f\x42\rPipelineProtob\x06proto3')
)




_PIPELINE = _descriptor.Descriptor(
  name='Pipeline',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inference_dsl', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.inference_dsl', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train_dsl', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.train_dsl', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train_runtime_conf', full_name='com.webank.ai.fate.core.mlmodel.buffer.Pipeline.train_runtime_conf', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['Pipeline'] = _PIPELINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pipeline = _reflection.GeneratedProtocolMessageType('Pipeline', (_message.Message,), dict(
  DESCRIPTOR = _PIPELINE,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.Pipeline)
  ))
_sym_db.RegisterMessage(Pipeline)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
