import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def setUp(self):
        self.parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.tag = "div"
        self.children = [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("div", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ])
            ]
        self.props = {
            "id": "content",
            "class": ".main-container",
        }

        self.default_html_string = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

    def test_parnet_node_creation(self):
        node = self.parent_node.to_html()
        self.assertEqual(node, self.default_html_string)

    def test_nested_parent_node_creation(self):
        node = ParentNode(self.tag, self.children, self.props).to_html()
        self.assertEqual(node, '<div id="content" class=".main-container"><b>Bold text</b>Normal text<i>italic text</i>Normal text<div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div></div>')

    if __name__ == "__main__":
        unittest.main()