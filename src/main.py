from textnode import TextNode
from leafnode import LeafNode

node = TextNode("test1", "bold", "www.test.com")
leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
print(node)
print(leafnode.to_html())

def text_node_to_html_node(text_node):
    match text_node["type"]:
        case "text":
            print("text")
        case "bold":
            print("bold")
        case "italic":
            print("italic")
        case "code":
            print("code")
        case "link":
            print("link")
        case "image":
            print("image")
