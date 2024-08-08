from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super(ParentNode, self).__init__(tag, value=None, children, props)

    def to_html(self):
        if tag is None:
            raise ValueError("an HTML tag is required")
        if children is None:
            raise ValueError("Parent Node requires a child object")
        return f"<{self.tag}>{self.children.to_html()}</{self.tag}>"
