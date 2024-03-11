import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_missing_url(self):
        node = TextNode("This is a text node", "bold", "https://example.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("This is a text node", "italic", "https://example.com")
        node2 = TextNode("This is a text node", "bold", "https://example.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "italic", "https://example.com")
        self.assertEqual(
            "TextNode(This is a text node, italic, https://example.com)",
            repr(node),
        )


if __name__ == "__main__":
    unittest.main()
