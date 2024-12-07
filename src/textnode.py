from enum import Enum
from leafnode import LeafNode
class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"
class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        if isinstance(text_type, TextType):
            self.text_type = text_type
        else:
            raise ValueError("Wrong text type value provided")
        self.url = url

    def __eq__(self, other_text_node):
        return self.text == other_text_node.text and self.text_type == other_text_node.text_type and self.url == other_text_node.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.NORMAL:
                return LeafNode(None, self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALIC:
                return LeafNode("i", self.text)
            case TextType.CODE:
                return LeafNode("code", self.text)
            case TextType.LINKS:
                return LeafNode("a", self.text, {"href": self.url})
            case TextType.IMAGES:
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
            case _:
                raise Exception("Invalid text node type")