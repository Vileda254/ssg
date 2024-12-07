import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.default_text = "This is a text node"

    def test_eq(self):
        node = TextNode(self.default_text, TextType.BOLD)
        node2 = TextNode(self.default_text, TextType.BOLD)
        self.assertEqual(node, node2)

    def test_missing_url(self):
        node_without_url = TextNode(self.default_text, TextType.BOLD)
        self.assertIsNone(node_without_url.url)

    def test_not_eq(self):
        node = TextNode(self.default_text, TextType.BOLD, "url.com")
        node2 = TextNode(self.default_text, TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_node_to_html(self):
        node = TextNode(self.default_text, TextType.LINKS, "url.com").text_node_to_html_node().to_html()
        self.assertEqual(node, '<a href="url.com">This is a text node</a>')

if __name__ == "__main__":
    unittest.main()