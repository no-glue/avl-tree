class AvlNode:
  def __init__(self, key, value, height = 0, left = None, right = None):
    """Set key and value for the node"""
    self.key = key
    self.value = value
    self.height = height
    self.left = left
    self.right = right
  def left(self):
    """Return left subtree"""
    return self.left
  def right(self):
    """Return right subtree"""
    return self.right
  def height(self):
    """Return own height"""
    return self.height
  def height(self, height):
    """Set own height"""
    self.height = height
    return self