from textnode import TextNode
from leafnode import LeafNode

node = TextNode("test1", "bold", "www.test.com")
leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
print(node)
print(leafnode.to_html())
