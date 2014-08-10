class AvlNode(object):
  def __init__(self, key = "", value = [], height = 0, left = None, right = None):
    """Set key and value for the node"""
    self._key = key
    self._value = value
    self._height = height
    self._left = left
    self._right = right
  @property
  def key(self):
    """Get key"""
    return self._key
  @key.setter
  def key(self, value):
    """Set key"""
    self._key = value
  @property
  def value(self):
    """Get value"""
    return self._value
  @value.setter
  def value(self, value):
    """Set value"""
    self._value = value
  @property
  def height(self):
    """Get height"""
    return self._height
  @height.setter
  def height(self, value):
    """Set own height"""
    self._height = value
  @property
  def left(self):
    """Get left"""
    return self._left
  @left.setter
  def left(self, value):
    """Set left"""
    self._left = value
  @property
  def right(self):
    """Get right"""
    return self._right
  @right.setter
  def right(self, value):
    """Set right"""
    self._right = value
  def spawn(self):
    """Spawn a node"""
    return AvlNode()
  def __str__(self):
    """Show self as string"""
    return "key: " + str(self.key) + "; value: " + str(self.value) + "; height: " + str(self.height)
