from textnode import TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            tN = LeafNode(None,text_node.text)
            print(tN.to_html())
        case "bold":
            tN = LeafNode("b",text_node.text)
            print(tN.to_html())
        case "italic":
            tN = LeafNode("i",text_node.text)
            print(tN.to_html())
        case "code":
            tN = LeafNode("code",text_node.text)
            print(tN.to_html())
        case "link":
            print("link")
            tN = LeafNode("a",text_node.text,{"href":text_node.url})
            print(tN.to_html())
        case "image":
            tN = LeafNode("img",None,{"src":text_node.url,"alt":text_node.text})
            print(tN.to_html())
        case _:
            raise Exception("Type does not exist.")

node = TextNode("test1", "bold", "www.test.com")
node2 = TextNode("I'm a link", "link", "www.test.com")
leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
print(node)
print(leafnode.to_html())
text_node_to_html_node(node) #Move to textnode.py text_node becomes self. 
text_node_to_html_node(node2)
