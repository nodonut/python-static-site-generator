import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode(
                    "b",
                    "Bold text",
                ),
                LeafNode(None, "Normal text"),
                LeafNode(
                    "i",
                    "italic text",
                ),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html(),
        )

    def test_to_html_with_parentnode(self):
        nested_parent_node = ParentNode(
            "a", [LeafNode(None, "Click "), ParentNode("i", [LeafNode("b", "Me")])]
        )

        self.assertEqual(
            "<a>Click <i><b>Me</b></i></a>",
            nested_parent_node.to_html(),
        )

    def test_to_html_with_props(self):
        node = ParentNode(
            "a",
            [
                LeafNode(None, "Click"),
                ParentNode("span", [LeafNode(None, "Me")], {"class": "my-class"}),
            ],
            {"href": "https://www.example.com", "download": True},
        )

        self.assertEqual(
            '<a href="https://www.example.com" download="True">Click<span class="my-class">Me</span></a>',
            node.to_html(),
        )


if __name__ == "__main__":
    unittest.main()
