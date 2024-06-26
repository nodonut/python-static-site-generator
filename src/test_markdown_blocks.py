import unittest
from markdown_blocks import (
    markdown_to_blocks,
    markdown_to_html_node,
    extract_title,
    block_to_block_type,
    block_type_ordered_list,
    block_type_code,
    block_type_unordered_list,
    block_type_quote,
    block_type_heading,
    block_type_paragraph,
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type(self):
        markdown = "1. Note 1\n2. Note 2"
        self.assertEqual(block_type_ordered_list, block_to_block_type(markdown))
        markdown = "* Note 1\n* Note 2"
        self.assertEqual(block_type_unordered_list, block_to_block_type(markdown))
        markdown = "- Note 1\n- Note 2"
        self.assertEqual(block_type_unordered_list, block_to_block_type(markdown))
        markdown = "```\ncode\n````"
        self.assertEqual(block_type_code, block_to_block_type(markdown))
        markdown = ">Quote\n>more quotes"
        self.assertEqual(block_type_quote, block_to_block_type(markdown))
        markdown = "paragraph"
        self.assertEqual(block_type_paragraph, block_to_block_type(markdown))
        markdown = "# Heading"
        self.assertEqual(block_type_heading, block_to_block_type(markdown))

    def test_markdown_to_html_nodes(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>This is <b>bolded</b> paragraph</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here This is the same paragraph on a new line</p><ul><li>This is a list</li><li>with items</li></ul></div>",
        )

    def test_extract_title(self):
        md = """
# This is heading 1

This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        title = extract_title(md)
        self.assertEqual("This is heading 1", title)


if __name__ == "__main__":
    unittest.main()
