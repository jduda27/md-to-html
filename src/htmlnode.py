class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("HTML conversion is not yet implemented")

    def props_to_html(self):
        result = " "
        for tag in self.props:
            result = result+tag+"=\""+self.props[tag]+"\" "
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"

    def __eq__(self, o):
        result = True
        if self.tag != o.tag:
            result = False
        if self.value != o.value:
            result = False
        if self.children != o.children:
            result = False
        if self.props != o.props:
            result = False
        return result
