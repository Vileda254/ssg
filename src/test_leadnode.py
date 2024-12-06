import unittest

from leafnode import LeafNode

class TestLeadNode(unittest.TestCase):
    def setUp(self):
        self.value = "Testing leaf node values"
        self.props = {
            "href": "http://www.mytest.com",
            "target": "_blank"
        }

    def test_missing_value(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode()
            node.to_html()

    def test_print_raw_value(self):
        node = LeafNode(value=self.value)
        raw_html_string = node.to_html()
        self.assertEqual(raw_html_string, "Testing leaf node values")

    def test_leafnode_created(self):
        node = LeafNode("a", self.value, self.props)
        html_string = node.to_html()
        self.assertEqual(html_string, '<a href="http://www.mytest.com" target="_blank">Testing leaf node values</a>')


if __name__ == "__main__":
    unittest.main()