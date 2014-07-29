class AvlTree:
  def __init__(self, root = None):
    """Initialize the tree, at first root is empty"""
    self.root = root
  def insert(self, node):
    """Insert a node"""
    self.root = self.insert(node, self.root)
  def insert(self, node, root):
    """Insert a node for real and give back root"""
    if not root:
      root = node
    elif node.key < root.key:
      root.left = self.insert(node, root.left)
      if root.left.height - root.right.height == 2:
        # Inserted node on the left side, check if left side is larger by 2
        # this is not allowed
        # at most 1 difference
        if node.key < root.left.key:
          root = self.rotateWithLeftChild(root)
        else:
          root = self.doubleWithLeftChild(root)
          # It's in wrong position, put it on the right
    elif node.key > root.key:
      root.right = self.insert(node, root.right)
      if root.right.height - root.left.height == 2:
        # Inserted node on the right side, check if right side larger by 2
        if node.key > root.right.key:
          root = self.rotateWithRightChild(root)
        else:
          root = self.doubleWithRightChild(root)
          # It's in wrong position, put it on the left
    else:
      # Duplicate happened, do nothing

    root.height = max(root.left.height, root.right.height) + 1
    # get root height, left or right subtree height + 1, depending which is greater
    return root
  def rotateWithLeftChild(node):
    """Rotate with left child"""
    temp = node
    # todo why the fuck i need temp?
    return_node = node.left
    temp.left = return_node.right

    return_node.right = temp

    # rotate to right
    return return_node