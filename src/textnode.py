class TextNode():
    def __init__(self, text="", text_type="", url="None"):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, o):
        result = True
        if self.text != o.text:
            result = False
        if self.text_type != o.text_type:
            result = False
        if self.url != o.url:
            result = False
        return result

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
