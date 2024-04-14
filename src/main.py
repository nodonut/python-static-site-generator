import os
import shutil
from textnode import TextNode
from copystatic import copy_dir_contents
from markdown_blocks import markdown_to_html_node, extract_title


def main():
    new_textnode = TextNode("This is a test node", "bold", "https://boot.dev")
    print(new_textnode)

    path = os.path.join(".", "static")
    dst = os.path.join(".", "public")
    content = os.path.join(".", "content")
    print(f"remove {dst}")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    print(f"begin copying data from {path}")
    copy_dir_contents(path, dst)
    print("copy completed")
    template_path = os.path.join(".", "template.html")
    generate_page_recursive(content, template_path, dst)


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    dir_list = os.listdir(dir_path_content)
    for dir in dir_list:
        full_path = os.path.join(dir_path_content, dir)
        if os.path.isfile(full_path):
            generate_page(
                full_path, template_path, os.path.join(dest_dir_path, "index.html")
            )
        if os.path.isdir(full_path):
            dest_full_path = os.path.join(dest_dir_path, dir)
            os.mkdir(dest_full_path)
            generate_page_recursive(full_path, template_path, dest_full_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = open(from_path)
    template = open(template_path)
    markdown_str = markdown.read()
    template_str = template.read()
    node = markdown_to_html_node(markdown_str)
    title = extract_title(markdown_str)
    with_title = template_str.replace("{{ Title }}", title)
    final = with_title.replace("{{ Content }}", node.to_html())
    html_file = open(dest_path, "w")
    html_file.write(final)

    markdown.close()
    template.close()
    html_file.close()


main()
