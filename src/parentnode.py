from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is missing")

        if self.children is None:
            raise ValueError("child nodes are required")

        result = ""
        for child in self.children:
            result += child.to_html()

        return result
