# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session/session.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='session/session.proto',
  package='session',
  syntax='proto3',
  serialized_pb=_b('\n\x15session/session.proto\x12\x07session\"=\n\x0eSessionMessage\x12\x15\n\rsession_token\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\tb\x06proto3')
)




_SESSIONMESSAGE = _descriptor.Descriptor(
  name='SessionMessage',
  full_name='session.SessionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_token', full_name='session.SessionMessage.session_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='session.SessionMessage.access_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=95,
)

DESCRIPTOR.message_types_by_name['SessionMessage'] = _SESSIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionMessage = _reflection.GeneratedProtocolMessageType('SessionMessage', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONMESSAGE,
  __module__ = 'session.session_pb2'
  # @@protoc_insertion_point(class_scope:session.SessionMessage)
  ))
_sym_db.RegisterMessage(SessionMessage)


# @@protoc_insertion_point(module_scope)
