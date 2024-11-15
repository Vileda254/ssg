import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        htmlChildNode = HTMLNode("p", "Text of a paragraph")
        self.tag = "a"
        self.value = "Testing of a value for a tag"
        self.children = [htmlChildNode]
        self.props = {
            "href": "http://www.mytest.com",
            "target": "_blank"
        }

    def test_props_to_html(self):
        htmlNode = HTMLNode(self.tag, self.value, props=self.props)
        props_string = htmlNode.props_to_html()
        self.assertEqual(props_string, f'href="{self.props["href"]}" target="{self.props["target"]}"')

if __name__ == "__main__":
    unittest.main()