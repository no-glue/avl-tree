class AvlNode:
  def __init__(self, key, value, height = 0, left = None, right = None):
    """Set key and value for the node"""
    self._key = key
    self._value = value
    self._height = height
    self._left = left
    self._right = right
    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, key):
        self._key = key
    @property
    def left(self):
      """Return left subtree"""
      return self._left
    @left.setter
    def left(self, node):
      """Set the left node"""
      self._left = node
    @property
    def right(self):
      """Return right subtree"""
      return self._right
    @right.setter
    def right(self, node):
      """Set the right node"""
      self._right = node
    @property
    def height(self):
      """Return own height"""
      return self._height
    @height.setter
    def height(self, height):
      """Set own height"""
      self._height = height