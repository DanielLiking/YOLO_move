# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from move_plan/BoundingBox.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class BoundingBox(genpy.Message):
  _md5sum = "34fcc54523e267db572de4c965cd93a3"
  _type = "move_plan/BoundingBox"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 probability
int64 xmin
int64 ymin
int64 xmax
int64 ymax
int16 num
string Class
string angle"""
  __slots__ = ['probability','xmin','ymin','xmax','ymax','num','Class','angle']
  _slot_types = ['float64','int64','int64','int64','int64','int16','string','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       probability,xmin,ymin,xmax,ymax,num,Class,angle

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BoundingBox, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.probability is None:
        self.probability = 0.
      if self.xmin is None:
        self.xmin = 0
      if self.ymin is None:
        self.ymin = 0
      if self.xmax is None:
        self.xmax = 0
      if self.ymax is None:
        self.ymax = 0
      if self.num is None:
        self.num = 0
      if self.Class is None:
        self.Class = ''
      if self.angle is None:
        self.angle = ''
    else:
      self.probability = 0.
      self.xmin = 0
      self.ymin = 0
      self.xmax = 0
      self.ymax = 0
      self.num = 0
      self.Class = ''
      self.angle = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_d4qh().pack(_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax, _x.num))
      _x = self.Class
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.angle
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 42
      (_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax, _x.num,) = _get_struct_d4qh().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Class = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Class = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.angle = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.angle = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_d4qh().pack(_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax, _x.num))
      _x = self.Class
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.angle
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 42
      (_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax, _x.num,) = _get_struct_d4qh().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Class = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Class = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.angle = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.angle = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_d4qh = None
def _get_struct_d4qh():
    global _struct_d4qh
    if _struct_d4qh is None:
        _struct_d4qh = struct.Struct("<d4qh")
    return _struct_d4qh
