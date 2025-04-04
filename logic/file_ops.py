# toolbelt/logic/file_ops.py

import os
import shutil


def move_file(src, dest) -> None:
    """Moves a file to a new directory."""
    shutil.move(src, dest)


def delete_file(path) -> None:
    """Deletes a file."""
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


def get_all_items(folder_path) -> list:
    """Gets a list of all the files/directories in a choosen directory."""
    file_list = []
    for root, dirs, files, in os.walk(folder_path):
        for name in dirs + files:
            file_list.append(os.path.join(root, name))
    return file_list


