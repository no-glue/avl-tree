from avl_node import AvlNode
from avl_tree import AvlTree

if __name__ == "__main__":
  keys = AvlTree()
  keys.insert(AvlNode("favorites", ["icecream", "chocolate", "coffee", "wine"]))
  print str(keys.find(AvlNode("favorites", "")).value)
  keys.insert(AvlNode("favorites", ["sugar"]))