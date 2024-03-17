import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
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
            "p",
        )

        self.assertEqual(
            "<b><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html(),
        )


if __name__ == "__main__":
    unittest.main()
