from avl_node import AvlNode
from avl_tree import AvlTree

if __name__ == "__main__":
  keys = AvlTree()

  keys.insert(AvlNode("name", "john"))
  keys.insert(AvlNode("lastname", "doe"))
  keys.insert(AvlNode("email", "john@doe.com"))
  keys.insert(AvlNode("address", "john doe 22"))
  keys.insert(AvlNode("phone", "12345"))
  keys.insert(AvlNode("nick", "johndoe"))
  keys.insert(AvlNode("country", "croatia"))
  keys.insert(AvlNode("favorites", ["icecream", "chocolate", "coffee", "wine"]))

  keys.print_tree()

  print str(keys.find(AvlNode("country", "")).value)

  keys.remove(AvlNode("country", ""))

  print str(keys.find(AvlNode("country", "")))

  print str(keys.find(AvlNode("favorites", "")).value)