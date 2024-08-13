from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super(ParentNode, self).__init__(tag, None, children, props)

    def to_html(self):
        childs = ""
        if self.tag is None:
            raise ValueError("an HTML tag is required")
        if self.children is None:
            raise ValueError("Parent Node requires a child object")
        for child in self.children:
            childs += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{childs}</{self.tag}>"
