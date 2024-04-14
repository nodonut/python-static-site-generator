from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)

    return children


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
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)

    return ParentNode("p", children)


def convert_block_to_heading(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break

    if level >= len(block):
        raise ValueError(f"Invalid heading level: {level}")

    text = block[level + 1 :]
    children = text_to_children(text)

    return ParentNode(f"h{level}", children)


def convert_block_to_code(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")

    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)

    return ParentNode("pre", [code])


def convert_block_to_blockquote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())

    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def convert_block_to_ul(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def convert_block_to_ol(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


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

    return ParentNode("div", children, None)


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    title = ""

    for block in blocks:
        if block.startswith("# "):
            title = block[2:]
            break

    if title == "":
        raise ValueError("Markdown must have a title")

    return title
