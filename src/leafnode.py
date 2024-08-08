from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super(LeafNode, self).__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("HTML Node must have a value.")
        if self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
