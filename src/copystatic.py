import os
import shutil


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
