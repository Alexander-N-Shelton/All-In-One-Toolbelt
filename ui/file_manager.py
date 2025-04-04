# toolbelt/ui/file_manager.py

import tkinter as tk
from tkinter import ttk, filedialog as fd, messagebox as msgbx
from logic.file_manager_controller import process_folder

class FileManagerTab(ttk.Frame):
    """File Manager Tab."""
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_opts = {'padx': 5, 'pady': 5}
        self._build_ui()

    def _build_ui(self):
        frame = ttk.LabelFrame(
            self, 
            text='Folder/File Manager', 
            borderwidth=10, 
            labelanchor='n'
        )
        frame.grid(
            column=0, 
            row=0, 
            sticky='N', 
            **self.grid_opts
        )

        # Folder path entry
        ttk.Label(
            frame, 
            text='Folder Path:'
        ).grid(
            column=0, 
            row=0, 
            sticky='W', 
            **self.grid_opts
        )

        self.folder_path = tk.StringVar()
        self.folder_entry = ttk.Entry(
            frame, 
            width=40, 
            textvariable=self.folder_path,
            font=(
                'Hack', 12,
            ),
        )
        self.folder_entry.grid(
            column=1, 
            row=0, 
            sticky='W', 
            **self.grid_opts
        )

        ttk.Button(
            frame, 
            text='Browse', 
            command=self.browse_folder,
            style='Large.TButton',
        ).grid(
            column=2, 
            row=0, 
            sticky='W', 
            **self.grid_opts
        )
        ttk.Button(
            frame, 
            text='Manage', 
            command=self.start_processing,
            style='Large.TButton',
        ).grid(
            column=0, 
            row=1, 
            columnspan=3, 
            sticky='S', 
            **self.grid_opts
        )

    def browse_folder(self):
        """Opens a file dialog for users to choose a directory/file."""
        folder = fd.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def start_processing(self):
        """Start going through the directory."""
        folder = self.folder_path.get()
        if folder:
            process_folder(folder, self)
        else:
            msgbx.showerror(
                "No Folder", 
                "Please select a folder first."
            )
