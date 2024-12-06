from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)  
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError("Missing value")
        if not self.tag:
            return f"{self.value}"

        if self.props:
            props_html = self.props_to_html()
            return f'<{self.tag} {props_html}>{self.value}</{self.tag}>'

        return f'<{self.tag}>{self.value}</{self.tag}>'
 

