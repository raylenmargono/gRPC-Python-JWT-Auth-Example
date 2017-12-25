# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kensho_service/kensho.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from session import session_pb2 as session_dot_session__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kensho_service/kensho.proto',
  package='kensho',
  syntax='proto3',
  serialized_pb=_b('\n\x1bkensho_service/kensho.proto\x12\x06kensho\x1a\x15session/session.proto\"@\n\rKenshoRequest\x12/\n\x0e\x61uthentication\x18\x01 \x01(\x0b\x32\x17.session.SessionMessage\"\x8f\x01\n\x0eKenshoResponse\x12\r\n\x05photo\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\x12\x19\n\x11\x65\x64ucation_snippet\x18\x05 \x01(\t\x12\x16\n\x0e\x63\x61reer_snippet\x18\x06 \x01(\t\"E\n\x12KenshoAdminRequest\x12/\n\x0e\x61uthentication\x18\x01 \x01(\x0b\x32\x17.session.SessionMessage\"\'\n\x13KenshoAdminResponse\x12\x10\n\x08response\x18\x01 \x01(\t2\x8f\x01\n\x06Kensho\x12;\n\x08\x44oKensho\x12\x15.kensho.KenshoRequest\x1a\x16.kensho.KenshoResponse0\x01\x12H\n\rDoAdminKensho\x12\x1a.kensho.KenshoAdminRequest\x1a\x1b.kensho.KenshoAdminResponseb\x06proto3')
  ,
  dependencies=[session_dot_session__pb2.DESCRIPTOR,])




_KENSHOREQUEST = _descriptor.Descriptor(
  name='KenshoRequest',
  full_name='kensho.KenshoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authentication', full_name='kensho.KenshoRequest.authentication', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=62,
  serialized_end=126,
)


_KENSHORESPONSE = _descriptor.Descriptor(
  name='KenshoResponse',
  full_name='kensho.KenshoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photo', full_name='kensho.KenshoResponse.photo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='kensho.KenshoResponse.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='kensho.KenshoResponse.first_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='kensho.KenshoResponse.last_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='education_snippet', full_name='kensho.KenshoResponse.education_snippet', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='career_snippet', full_name='kensho.KenshoResponse.career_snippet', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=129,
  serialized_end=272,
)


_KENSHOADMINREQUEST = _descriptor.Descriptor(
  name='KenshoAdminRequest',
  full_name='kensho.KenshoAdminRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authentication', full_name='kensho.KenshoAdminRequest.authentication', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=274,
  serialized_end=343,
)


_KENSHOADMINRESPONSE = _descriptor.Descriptor(
  name='KenshoAdminResponse',
  full_name='kensho.KenshoAdminResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='kensho.KenshoAdminResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=345,
  serialized_end=384,
)

_KENSHOREQUEST.fields_by_name['authentication'].message_type = session_dot_session__pb2._SESSIONMESSAGE
_KENSHOADMINREQUEST.fields_by_name['authentication'].message_type = session_dot_session__pb2._SESSIONMESSAGE
DESCRIPTOR.message_types_by_name['KenshoRequest'] = _KENSHOREQUEST
DESCRIPTOR.message_types_by_name['KenshoResponse'] = _KENSHORESPONSE
DESCRIPTOR.message_types_by_name['KenshoAdminRequest'] = _KENSHOADMINREQUEST
DESCRIPTOR.message_types_by_name['KenshoAdminResponse'] = _KENSHOADMINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KenshoRequest = _reflection.GeneratedProtocolMessageType('KenshoRequest', (_message.Message,), dict(
  DESCRIPTOR = _KENSHOREQUEST,
  __module__ = 'kensho_service.kensho_pb2'
  # @@protoc_insertion_point(class_scope:kensho.KenshoRequest)
  ))
_sym_db.RegisterMessage(KenshoRequest)

KenshoResponse = _reflection.GeneratedProtocolMessageType('KenshoResponse', (_message.Message,), dict(
  DESCRIPTOR = _KENSHORESPONSE,
  __module__ = 'kensho_service.kensho_pb2'
  # @@protoc_insertion_point(class_scope:kensho.KenshoResponse)
  ))
_sym_db.RegisterMessage(KenshoResponse)

KenshoAdminRequest = _reflection.GeneratedProtocolMessageType('KenshoAdminRequest', (_message.Message,), dict(
  DESCRIPTOR = _KENSHOADMINREQUEST,
  __module__ = 'kensho_service.kensho_pb2'
  # @@protoc_insertion_point(class_scope:kensho.KenshoAdminRequest)
  ))
_sym_db.RegisterMessage(KenshoAdminRequest)

KenshoAdminResponse = _reflection.GeneratedProtocolMessageType('KenshoAdminResponse', (_message.Message,), dict(
  DESCRIPTOR = _KENSHOADMINRESPONSE,
  __module__ = 'kensho_service.kensho_pb2'
  # @@protoc_insertion_point(class_scope:kensho.KenshoAdminResponse)
  ))
_sym_db.RegisterMessage(KenshoAdminResponse)



_KENSHO = _descriptor.ServiceDescriptor(
  name='Kensho',
  full_name='kensho.Kensho',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=387,
  serialized_end=530,
  methods=[
  _descriptor.MethodDescriptor(
    name='DoKensho',
    full_name='kensho.Kensho.DoKensho',
    index=0,
    containing_service=None,
    input_type=_KENSHOREQUEST,
    output_type=_KENSHORESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DoAdminKensho',
    full_name='kensho.Kensho.DoAdminKensho',
    index=1,
    containing_service=None,
    input_type=_KENSHOADMINREQUEST,
    output_type=_KENSHOADMINRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_KENSHO)

DESCRIPTOR.services_by_name['Kensho'] = _KENSHO

# @@protoc_insertion_point(module_scope)
