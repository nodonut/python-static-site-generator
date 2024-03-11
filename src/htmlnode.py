class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return

        output = ""
        for key in self.props:
            output += f" {key}={self.props[key]}"

        return output

    def __repr__(self):
        return f"<{self.tag} {self.props}>{self.value}{self.children}</{self.tag}>"
