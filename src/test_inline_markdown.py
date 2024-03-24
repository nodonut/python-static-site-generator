import unittest

from inline_markdown import (
    split_nodes_delimiter,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is a **text** with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
            [
                TextNode("This is a ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
