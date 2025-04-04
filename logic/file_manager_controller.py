# logic/file_manager_controller.py

from logic.file_ops import get_all_items
from ui.pop_up import show_action_popup


def process_folder(folder_path, parent, file_list=None, index=0) -> None:
    """Processes the folders/files one at a time."""
    if file_list is None:
        file_list = get_all_items(folder_path)

    if index < len(file_list):
        file_path = file_list[index]

        def on_complete():
            process_folder(folder_path, parent, file_list, index + 1)

        show_action_popup(file_path, on_complete, parent)
