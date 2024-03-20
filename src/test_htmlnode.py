import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {"href": "https://example.com", "download": True}
        node = HTMLNode("a", "Click me", None, props)
        self.assertEqual(
            ' href="https://example.com" download="True"', node.props_to_html()
        )


if __name__ == "__main__":
    unittest.main()
