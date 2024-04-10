import os
import shutil
from textnode import TextNode


def main():
    new_textnode = TextNode("This is a test node", "bold", "https://boot.dev")
    print(new_textnode)

    path = os.path.join(".", "static")
    dst = os.path.join(".", "public")
    print(f"remove {dst}")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    print(f"begin copying data from {path}")
    copy_dir_contents(path, dst)
    print("copy completed")


def copy_dir_contents(path, dst):
    if not os.path.exists(path):
        raise ValueError("provided path does not exist")

    print("listing dirs")
    dir_list = os.listdir(path)
    for dir in dir_list:
        full_path = os.path.join(path, dir)
        print(full_path)
        if os.path.isfile(full_path):
            print(f"copying file {full_path} to {dst}")
            shutil.copy(full_path, dst)
        if os.path.isdir(full_path):
            print(f"copying dir {full_path} to {dst}")
            dir_full_path = os.path.join(dst, dir)
            os.mkdir(dir_full_path)
            copy_dir_contents(full_path, dir_full_path)


main()
