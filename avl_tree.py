class AvlTree(object):
  def __init__(self, root = None):
    """Initialize the tree, at first root is empty"""
    self.root = root
  def insert(self, node, root = None):
    """Insert a node"""
    self.root = self._insert(node, root if root else self.root)
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
    else:
      root.value.extend(node.value)

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
  def find(self, node, root = None):
    """Find a key"""
    return self._find(node, root if root else self.root)
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
  def remove(self, node, root = None):
    """Remove node"""
    self.root = self._remove(node, root if root else self.root)
  def _remove(self, node, root):
    """Remove a node for real and give back root"""
    if not root:
      return root
      # key is not found, do nothing
    if node.key < root.key:
      root.left = self._remove(node, root.left)
      # removed element from tree, rebalance it
      if root.right and root.right.height - root.left.height == 2:
        # tree is unbalanced, balance it
        right_height = root.right.right.height if root.right.right else 0
        left_height = root.right.left.height if root.right.left else 0
        if right_height >= left_height:
          root = self.rotate_with_left_child(root)
        else:
          root = self.double_with_right_child(root)
    elif node.key > root.key:
      root.right = self._remove(node, root.right)
      # removed element from tree, rebalance it
      if root.left and root.left.height - root.right.height == 2:
        # tree is unbalanced, balance it
        right_height = root.left.right.height if root.left.right else 0
        left_height = root.left.left.height if root.left.left else 0
        if left_height >= right_height:
          root = self.rotate_with_right_child(root)
        else:
          root = self.double_with_left_child(root)
    elif root.left:
      # node to be removed, pick largest one and move it to root
      max_node = self._find_max(root.left) # todo
      root.key = max_node.key
      root.value = max_node.value
      self._remove(max_node, root.left)
      # removed from left side, rebalance
      if root.right and root.right.height - root.left.height == 2:
        # tree in unbalanced, balance it
        right_height = root.right.right.height if root.right.right else 0
        left_height = root.right.left.height if root.right.left else 0
        if right_height >= left_height:
          root = self.rotate_with_left_child(root)
        else:
          root = self.double_with_right_child(root)
    else:
      root = root.left if root.left else root.right
    if root:
      root.height = max(root.left.height if root.left else -1, root.right.height if root.right else -1) + 1
    return root
  def find_max(self, root = None):
    """Find largest node in tree"""
    return self._find_max(root if root else self.root)
  def _find_max(self, root):
    """Find largest node in tree"""
    while root.right:
      root = root.right
    return root
  def print_tree(self, root = None, direction = None):
    """Prints tree"""
    self._print_tree(self.root if not root else root, "" if not direction else direction)
  def _print_tree(self, root, direction):
    """Prints tree"""
    if root:
      self._print_tree(root.left, "l")
      print direction + " " + str(root)
      self._print_tree(root.right, "r")
