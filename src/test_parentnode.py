import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode(
                    "Bold text",
                    "b",
                ),
                LeafNode("Normal text", None),
                LeafNode(
                    "italic text",
                    "i",
                ),
                LeafNode("Normal text", None),
            ],
        )

        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html(),
        )

    def test_to_html_with_parentnode(self):
        nested_parent_node = ParentNode(
            "a", [LeafNode("Click ", None), ParentNode("i", [LeafNode("Me", "b")])]
        )

        self.assertEqual(
            "<a>Click <i><b>Me</b></i></a>",
            nested_parent_node.to_html(),
        )

    def test_to_html_with_props(self):
        node = ParentNode(
            "a",
            [
                LeafNode("Click", None),
                ParentNode("span", [LeafNode("Me", None)], {"class": "my-class"}),
            ],
            {"href": "https://www.example.com", "download": True},
        )

        self.assertEqual(
            '<a href="https://www.example.com" download="True">Click<span class="my-class">Me</span></a>',
            node.to_html(),
        )


if __name__ == "__main__":
    unittest.main()
