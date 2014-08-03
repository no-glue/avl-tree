class AvlTree(object):
  def __init__(self, root = None):
    """Initialize the tree, at first root is empty"""
    self.root = root
  def insert(self, node):
    """Insert a node"""
    self.root = self._insert(node, self.root)
  def _insert(self, node, root):
    """Insert a node for real and give back root"""
    if not root:
      root = node
    elif node.key < root.key:
      root.left = self._insert(node, root.left)
      if root.right and (root.left.height - root.right.height == 2):
        # Inserted node on the left side, check if left side is larger by 2
        # this is not allowed
        # at most 1 difference
        if node.key < root.left.key:
          root = self.rotate_with_left_child(root)
        else:
          root = self.double_with_left_child(root)
          # It's in wrong position, put it on the right
    elif node.key > root.key:
      root.right = self._insert(node, root.right)
      if root.left and (root.right.height - root.left.height == 2):
        # Inserted node on the right side, check if right side larger by 2
        # not allowed
        # max 1 difference
        if node.key > root.right.key:
          root = self.rotate_with_right_child(root)
        else:
          root = self.double_with_right_child(root)
          # It's in wrong position, put it on the left

    root.height = max(root.left.height if root.left else -1, root.right.height if root.right else -1) + 1
    # get root height, left or right subtree height + 1, depending which is greater
    return root
  def rotate_with_left_child(self, node):
    """Rotate with left child"""
    temp = node
    # todo why the fuck i need temp?
    return_node = node.left
    temp.left = return_node.right

    return_node.right = temp

    # rotate to right
    return return_node
  def rotate_with_right_child(self, node):
    """Rotate with right child"""
    temp = node
    # todo why the fuck i need temp?
    return_node = node.right
    temp.right = return_node.left

    return_node.left = temp

    # rotate to left
    return return_node
  def double_with_left_child(self, node):
    """Double rotate with left child"""
    node.left = self.rotate_with_right_child(node.left)
    # double rotate to the right
    return self.rotate_with_left_child(node)
  def double_with_right_child(self, node):
    """Double rotate with right child"""
    node.right = self.rotate_with_left_child(node.right)
    # double rotate to the left
    return self.rotate_with_right_child(node)
  def find(self, node):
    """Find a key"""
    return self._find(node, self.root)
  def _find(self, node, root):
    """Find for real"""
    while root:
      if node.key == root.key:
        return root
      if node.key > root.key:
        root = root.right
      else:
        root = root.left
    return root
  def remove(self, node):
    """Remove node"""
    self.root = self.remove(node, self.root)
  def remove(self, node, root):
    """Remove a node for real and give back root"""
    # if remove from left, check if smaller by 2
    # if yes do rotations
    # if remove from right, check if smaller by 2
    # if yes do rotations