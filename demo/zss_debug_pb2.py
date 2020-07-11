# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zss_debug.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='zss_debug.proto',
  package='ZSS.Protocol',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0fzss_debug.proto\x12\x0cZSS.Protocol\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\"U\n\tRectangle\x12#\n\x06point1\x18\x01 \x02(\x0b\x32\x13.ZSS.Protocol.Point\x12#\n\x06point2\x18\x02 \x02(\x0b\x32\x13.ZSS.Protocol.Point\"<\n\x0b\x44\x65\x62ug_Robot\x12 \n\x03pos\x18\x01 \x02(\x0b\x32\x13.ZSS.Protocol.Point\x12\x0b\n\x03\x64ir\x18\x02 \x02(\x02\"q\n\nDebug_Line\x12\"\n\x05start\x18\x01 \x02(\x0b\x32\x13.ZSS.Protocol.Point\x12 \n\x03\x65nd\x18\x02 \x02(\x0b\x32\x13.ZSS.Protocol.Point\x12\x0f\n\x07\x46ORWARD\x18\x03 \x02(\x08\x12\x0c\n\x04\x42\x41\x43K\x18\x04 \x02(\x08\"a\n\tDebug_Arc\x12*\n\trectangle\x18\x01 \x02(\x0b\x32\x17.ZSS.Protocol.Rectangle\x12\r\n\x05start\x18\x02 \x02(\x02\x12\x0b\n\x03\x65nd\x18\x03 \x02(\x02\x12\x0c\n\x04\x46ILL\x18\x04 \x02(\x08\"B\n\rDebug_Polygon\x12#\n\x06vertex\x18\x01 \x03(\x0b\x32\x13.ZSS.Protocol.Point\x12\x0c\n\x04\x46ILL\x18\x02 \x02(\x08\"<\n\nDebug_Text\x12 \n\x03pos\x18\x01 \x02(\x0b\x32\x13.ZSS.Protocol.Point\x12\x0c\n\x04text\x18\x02 \x02(\t\"?\n\x0c\x44\x65\x62ug_Curve_\x12\x0b\n\x03num\x18\x01 \x02(\x02\x12\x10\n\x08maxLimit\x18\x02 \x02(\x02\x12\x10\n\x08minLimit\x18\x03 \x02(\x02\"\x95\x01\n\x0b\x44\x65\x62ug_Curve\x12\"\n\x05start\x18\x01 \x02(\x0b\x32\x13.ZSS.Protocol.Point\x12\x1f\n\x02p1\x18\x02 \x02(\x0b\x32\x13.ZSS.Protocol.Point\x12\x1f\n\x02p2\x18\x03 \x02(\x0b\x32\x13.ZSS.Protocol.Point\x12 \n\x03\x65nd\x18\x04 \x02(\x0b\x32\x13.ZSS.Protocol.Point\"2\n\x0c\x44\x65\x62ug_Points\x12\"\n\x05point\x18\x01 \x03(\x0b\x32\x13.ZSS.Protocol.Point\"\x80\x05\n\tDebug_Msg\x12\x30\n\x04type\x18\x01 \x02(\x0e\x32\".ZSS.Protocol.Debug_Msg.Debug_Type\x12,\n\x05\x63olor\x18\x02 \x02(\x0e\x32\x1d.ZSS.Protocol.Debug_Msg.Color\x12$\n\x03\x61rc\x18\x03 \x01(\x0b\x32\x17.ZSS.Protocol.Debug_Arc\x12&\n\x04line\x18\x04 \x01(\x0b\x32\x18.ZSS.Protocol.Debug_Line\x12&\n\x04text\x18\x05 \x01(\x0b\x32\x18.ZSS.Protocol.Debug_Text\x12(\n\x05robot\x18\x06 \x01(\x0b\x32\x19.ZSS.Protocol.Debug_Robot\x12)\n\x05\x63urve\x18\x07 \x01(\x0b\x32\x1a.ZSS.Protocol.Debug_Curve_\x12,\n\x07polygon\x18\x08 \x01(\x0b\x32\x1b.ZSS.Protocol.Debug_Polygon\x12*\n\x06points\x18\t \x01(\x0b\x32\x1a.ZSS.Protocol.Debug_Points\x12\x11\n\tRGB_value\x18\n \x01(\x05\"X\n\nDebug_Type\x12\x07\n\x03\x41RC\x10\x00\x12\x08\n\x04LINE\x10\x01\x12\x08\n\x04TEXT\x10\x02\x12\t\n\x05ROBOT\x10\x03\x12\t\n\x05\x43URVE\x10\x04\x12\x0b\n\x07POLYGON\x10\x05\x12\n\n\x06Points\x10\x06\"\x80\x01\n\x05\x43olor\x12\t\n\x05WHITE\x10\x00\x12\x07\n\x03RED\x10\x01\x12\n\n\x06ORANGE\x10\x02\x12\n\n\x06YELLOW\x10\x03\x12\t\n\x05GREEN\x10\x04\x12\x08\n\x04\x43YAN\x10\x05\x12\x08\n\x04\x42LUE\x10\x06\x12\n\n\x06PURPLE\x10\x07\x12\x08\n\x04GRAY\x10\x08\x12\t\n\x05\x42LACK\x10\t\x12\x0b\n\x07USE_RGB\x10\n\"3\n\nDebug_Msgs\x12%\n\x04msgs\x18\x01 \x03(\x0b\x32\x17.ZSS.Protocol.Debug_Msg\"<\n\x0b\x44\x65\x62ug_Score\x12\r\n\x05\x63olor\x18\x01 \x02(\x05\x12\x1e\n\x01p\x18\x02 \x03(\x0b\x32\x13.ZSS.Protocol.Point\"9\n\x0c\x44\x65\x62ug_Scores\x12)\n\x06scores\x18\x01 \x03(\x0b\x32\x19.ZSS.Protocol.Debug_Score')
)



_DEBUG_MSG_DEBUG_TYPE = _descriptor.EnumDescriptor(
  name='Debug_Type',
  full_name='ZSS.Protocol.Debug_Msg.Debug_Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ARC', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CURVE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POLYGON', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Points', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1248,
  serialized_end=1336,
)
_sym_db.RegisterEnumDescriptor(_DEBUG_MSG_DEBUG_TYPE)

_DEBUG_MSG_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='ZSS.Protocol.Debug_Msg.Color',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WHITE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORANGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREEN', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CYAN', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLUE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PURPLE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAY', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLACK', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_RGB', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1339,
  serialized_end=1467,
)
_sym_db.RegisterEnumDescriptor(_DEBUG_MSG_COLOR)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='ZSS.Protocol.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='ZSS.Protocol.Point.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='ZSS.Protocol.Point.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=62,
)


_RECTANGLE = _descriptor.Descriptor(
  name='Rectangle',
  full_name='ZSS.Protocol.Rectangle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point1', full_name='ZSS.Protocol.Rectangle.point1', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point2', full_name='ZSS.Protocol.Rectangle.point2', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=149,
)


_DEBUG_ROBOT = _descriptor.Descriptor(
  name='Debug_Robot',
  full_name='ZSS.Protocol.Debug_Robot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos', full_name='ZSS.Protocol.Debug_Robot.pos', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dir', full_name='ZSS.Protocol.Debug_Robot.dir', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=211,
)


_DEBUG_LINE = _descriptor.Descriptor(
  name='Debug_Line',
  full_name='ZSS.Protocol.Debug_Line',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='ZSS.Protocol.Debug_Line.start', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='ZSS.Protocol.Debug_Line.end', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FORWARD', full_name='ZSS.Protocol.Debug_Line.FORWARD', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BACK', full_name='ZSS.Protocol.Debug_Line.BACK', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=326,
)


_DEBUG_ARC = _descriptor.Descriptor(
  name='Debug_Arc',
  full_name='ZSS.Protocol.Debug_Arc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rectangle', full_name='ZSS.Protocol.Debug_Arc.rectangle', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='ZSS.Protocol.Debug_Arc.start', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='ZSS.Protocol.Debug_Arc.end', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FILL', full_name='ZSS.Protocol.Debug_Arc.FILL', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=425,
)


_DEBUG_POLYGON = _descriptor.Descriptor(
  name='Debug_Polygon',
  full_name='ZSS.Protocol.Debug_Polygon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertex', full_name='ZSS.Protocol.Debug_Polygon.vertex', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FILL', full_name='ZSS.Protocol.Debug_Polygon.FILL', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=493,
)


_DEBUG_TEXT = _descriptor.Descriptor(
  name='Debug_Text',
  full_name='ZSS.Protocol.Debug_Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos', full_name='ZSS.Protocol.Debug_Text.pos', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='ZSS.Protocol.Debug_Text.text', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=555,
)


_DEBUG_CURVE_ = _descriptor.Descriptor(
  name='Debug_Curve_',
  full_name='ZSS.Protocol.Debug_Curve_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='ZSS.Protocol.Debug_Curve_.num', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxLimit', full_name='ZSS.Protocol.Debug_Curve_.maxLimit', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minLimit', full_name='ZSS.Protocol.Debug_Curve_.minLimit', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=557,
  serialized_end=620,
)


_DEBUG_CURVE = _descriptor.Descriptor(
  name='Debug_Curve',
  full_name='ZSS.Protocol.Debug_Curve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='ZSS.Protocol.Debug_Curve.start', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p1', full_name='ZSS.Protocol.Debug_Curve.p1', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p2', full_name='ZSS.Protocol.Debug_Curve.p2', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='ZSS.Protocol.Debug_Curve.end', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=623,
  serialized_end=772,
)


_DEBUG_POINTS = _descriptor.Descriptor(
  name='Debug_Points',
  full_name='ZSS.Protocol.Debug_Points',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='ZSS.Protocol.Debug_Points.point', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=774,
  serialized_end=824,
)


_DEBUG_MSG = _descriptor.Descriptor(
  name='Debug_Msg',
  full_name='ZSS.Protocol.Debug_Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ZSS.Protocol.Debug_Msg.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='ZSS.Protocol.Debug_Msg.color', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arc', full_name='ZSS.Protocol.Debug_Msg.arc', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line', full_name='ZSS.Protocol.Debug_Msg.line', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='ZSS.Protocol.Debug_Msg.text', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robot', full_name='ZSS.Protocol.Debug_Msg.robot', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curve', full_name='ZSS.Protocol.Debug_Msg.curve', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='polygon', full_name='ZSS.Protocol.Debug_Msg.polygon', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='ZSS.Protocol.Debug_Msg.points', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RGB_value', full_name='ZSS.Protocol.Debug_Msg.RGB_value', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEBUG_MSG_DEBUG_TYPE,
    _DEBUG_MSG_COLOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=827,
  serialized_end=1467,
)


_DEBUG_MSGS = _descriptor.Descriptor(
  name='Debug_Msgs',
  full_name='ZSS.Protocol.Debug_Msgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgs', full_name='ZSS.Protocol.Debug_Msgs.msgs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1469,
  serialized_end=1520,
)


_DEBUG_SCORE = _descriptor.Descriptor(
  name='Debug_Score',
  full_name='ZSS.Protocol.Debug_Score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='ZSS.Protocol.Debug_Score.color', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p', full_name='ZSS.Protocol.Debug_Score.p', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1522,
  serialized_end=1582,
)


_DEBUG_SCORES = _descriptor.Descriptor(
  name='Debug_Scores',
  full_name='ZSS.Protocol.Debug_Scores',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scores', full_name='ZSS.Protocol.Debug_Scores.scores', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1584,
  serialized_end=1641,
)

_RECTANGLE.fields_by_name['point1'].message_type = _POINT
_RECTANGLE.fields_by_name['point2'].message_type = _POINT
_DEBUG_ROBOT.fields_by_name['pos'].message_type = _POINT
_DEBUG_LINE.fields_by_name['start'].message_type = _POINT
_DEBUG_LINE.fields_by_name['end'].message_type = _POINT
_DEBUG_ARC.fields_by_name['rectangle'].message_type = _RECTANGLE
_DEBUG_POLYGON.fields_by_name['vertex'].message_type = _POINT
_DEBUG_TEXT.fields_by_name['pos'].message_type = _POINT
_DEBUG_CURVE.fields_by_name['start'].message_type = _POINT
_DEBUG_CURVE.fields_by_name['p1'].message_type = _POINT
_DEBUG_CURVE.fields_by_name['p2'].message_type = _POINT
_DEBUG_CURVE.fields_by_name['end'].message_type = _POINT
_DEBUG_POINTS.fields_by_name['point'].message_type = _POINT
_DEBUG_MSG.fields_by_name['type'].enum_type = _DEBUG_MSG_DEBUG_TYPE
_DEBUG_MSG.fields_by_name['color'].enum_type = _DEBUG_MSG_COLOR
_DEBUG_MSG.fields_by_name['arc'].message_type = _DEBUG_ARC
_DEBUG_MSG.fields_by_name['line'].message_type = _DEBUG_LINE
_DEBUG_MSG.fields_by_name['text'].message_type = _DEBUG_TEXT
_DEBUG_MSG.fields_by_name['robot'].message_type = _DEBUG_ROBOT
_DEBUG_MSG.fields_by_name['curve'].message_type = _DEBUG_CURVE_
_DEBUG_MSG.fields_by_name['polygon'].message_type = _DEBUG_POLYGON
_DEBUG_MSG.fields_by_name['points'].message_type = _DEBUG_POINTS
_DEBUG_MSG_DEBUG_TYPE.containing_type = _DEBUG_MSG
_DEBUG_MSG_COLOR.containing_type = _DEBUG_MSG
_DEBUG_MSGS.fields_by_name['msgs'].message_type = _DEBUG_MSG
_DEBUG_SCORE.fields_by_name['p'].message_type = _POINT
_DEBUG_SCORES.fields_by_name['scores'].message_type = _DEBUG_SCORE
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Rectangle'] = _RECTANGLE
DESCRIPTOR.message_types_by_name['Debug_Robot'] = _DEBUG_ROBOT
DESCRIPTOR.message_types_by_name['Debug_Line'] = _DEBUG_LINE
DESCRIPTOR.message_types_by_name['Debug_Arc'] = _DEBUG_ARC
DESCRIPTOR.message_types_by_name['Debug_Polygon'] = _DEBUG_POLYGON
DESCRIPTOR.message_types_by_name['Debug_Text'] = _DEBUG_TEXT
DESCRIPTOR.message_types_by_name['Debug_Curve_'] = _DEBUG_CURVE_
DESCRIPTOR.message_types_by_name['Debug_Curve'] = _DEBUG_CURVE
DESCRIPTOR.message_types_by_name['Debug_Points'] = _DEBUG_POINTS
DESCRIPTOR.message_types_by_name['Debug_Msg'] = _DEBUG_MSG
DESCRIPTOR.message_types_by_name['Debug_Msgs'] = _DEBUG_MSGS
DESCRIPTOR.message_types_by_name['Debug_Score'] = _DEBUG_SCORE
DESCRIPTOR.message_types_by_name['Debug_Scores'] = _DEBUG_SCORES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Point)
  })
_sym_db.RegisterMessage(Point)

Rectangle = _reflection.GeneratedProtocolMessageType('Rectangle', (_message.Message,), {
  'DESCRIPTOR' : _RECTANGLE,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Rectangle)
  })
_sym_db.RegisterMessage(Rectangle)

Debug_Robot = _reflection.GeneratedProtocolMessageType('Debug_Robot', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_ROBOT,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Robot)
  })
_sym_db.RegisterMessage(Debug_Robot)

Debug_Line = _reflection.GeneratedProtocolMessageType('Debug_Line', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_LINE,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Line)
  })
_sym_db.RegisterMessage(Debug_Line)

Debug_Arc = _reflection.GeneratedProtocolMessageType('Debug_Arc', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_ARC,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Arc)
  })
_sym_db.RegisterMessage(Debug_Arc)

Debug_Polygon = _reflection.GeneratedProtocolMessageType('Debug_Polygon', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_POLYGON,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Polygon)
  })
_sym_db.RegisterMessage(Debug_Polygon)

Debug_Text = _reflection.GeneratedProtocolMessageType('Debug_Text', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_TEXT,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Text)
  })
_sym_db.RegisterMessage(Debug_Text)

Debug_Curve_ = _reflection.GeneratedProtocolMessageType('Debug_Curve_', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_CURVE_,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Curve_)
  })
_sym_db.RegisterMessage(Debug_Curve_)

Debug_Curve = _reflection.GeneratedProtocolMessageType('Debug_Curve', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_CURVE,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Curve)
  })
_sym_db.RegisterMessage(Debug_Curve)

Debug_Points = _reflection.GeneratedProtocolMessageType('Debug_Points', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_POINTS,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Points)
  })
_sym_db.RegisterMessage(Debug_Points)

Debug_Msg = _reflection.GeneratedProtocolMessageType('Debug_Msg', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_MSG,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Msg)
  })
_sym_db.RegisterMessage(Debug_Msg)

Debug_Msgs = _reflection.GeneratedProtocolMessageType('Debug_Msgs', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_MSGS,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Msgs)
  })
_sym_db.RegisterMessage(Debug_Msgs)

Debug_Score = _reflection.GeneratedProtocolMessageType('Debug_Score', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_SCORE,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Score)
  })
_sym_db.RegisterMessage(Debug_Score)

Debug_Scores = _reflection.GeneratedProtocolMessageType('Debug_Scores', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG_SCORES,
  '__module__' : 'zss_debug_pb2'
  # @@protoc_insertion_point(class_scope:ZSS.Protocol.Debug_Scores)
  })
_sym_db.RegisterMessage(Debug_Scores)


# @@protoc_insertion_point(module_scope)
