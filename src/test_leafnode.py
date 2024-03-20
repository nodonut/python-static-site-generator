import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("this is a paragraph", "p")
        self.assertEqual("<p>this is a paragraph</p>", node.to_html())

    def test_to_html_with_props(self):
        props = {"href": "https://example.com"}
        node = LeafNode("this is a paragraph", "p", props)
        self.assertEqual(
            '<p href="https://example.com">this is a paragraph</p>', node.to_html()
        )


if __name__ == "__main__":
    unittest.main()
