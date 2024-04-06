from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote

    if block.startswith(("* ", "- ")):
        for line in lines:
            if not line.startswith(("* ", "- ")):
                return block_type_paragraph
        return block_type_unordered_list

    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list

    return block_type_paragraph


def convert_block_to_paragraph(block):
    children = []

    for text_node in text_to_textnodes(block):
        node = text_node_to_html_node(text_node)
        children.append(node)

    return ParentNode("p", children)


def convert_block_to_heading(block):
    heading = ""
    if block.startswith("# "):
        heading = "h1"
    elif block.startswith("## "):
        heading = "h2"
    elif block.startswith("### "):
        heading = "h3"
    elif block.startswith("#### "):
        heading = "h4"
    elif block.startswith("##### "):
        heading = "h5"
    elif block.startswith("###### "):
        heading = "h6"

    return LeafNode(f"h{heading}", block)


def convert_block_to_code(block):
    return ParentNode("pre", [HTMLNode("code", block)])


def convert_block_to_blockquote(block):
    return LeafNode("blockquote", block)


def convert_block_to_ul(block):
    return ParentNode("ul", map(lambda line: LeafNode("li", line), block.split("\n")))


def convert_block_to_ol(block):
    return ParentNode("ol", map(lambda line: LeafNode("li", line), block.split("\n")))


def convert_block_to_html_node(block, block_type):
    if block_type == block_type_quote:
        return convert_block_to_blockquote(block)
    elif block_type == block_type_code:
        return convert_block_to_code(block)
    elif block_type == block_type_heading:
        return convert_block_to_heading(block)
    elif block_type == block_type_unordered_list:
        return convert_block_to_ul(block)
    elif block_type == block_type_ordered_list:
        return convert_block_to_ol(block)
    else:
        return convert_block_to_paragraph(block)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        node = convert_block_to_html_node(block, block_type)
        children.append(node)

    return ParentNode("div", children)
