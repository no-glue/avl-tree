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
    root.height = max(root.left.height, root.right.height) + 1
    # get root height, left or right subtree height + 1, depending which is greater
    return root