# components/pop_up.py

import os
import tkinter as tk
from tkinter import ttk, filedialog as fd, messagebox as msgbx
from logic.file_ops import move_file, delete_file


def show_action_popup(file_path, on_complete, parent):
    """PopUp window that provides the options for managing files/directories."""
    top = tk.Toplevel(parent)
    top.title('Process File/Folder')

    frame = ttk.LabelFrame(
        top, 
        text='Choose What To Do'
    )
    frame.grid(
        column=0, 
        row=0, 
        padx=5, 
        pady=5
    )

    ttk.Label(
        frame, 
        text=f"What would you like to do with:\n{file_path}"
    ).grid(
        column=0, 
        row=0, 
        columnspan=3, 
        sticky='W', 
        padx=5, 
        pady=5
    )

    def next():
        """Proceed to the next."""
        top.destroy()
        on_complete()

    def move():
        """Move the file."""
        dest = fd.askdirectory(
            title="Select Destination", 
            parent=top
        )
        if dest:
            try:
                move_file(file_path, dest)
                msgbx.showinfo(
                    title="Success", 
                    message=f"{os.path.basename(file_path)} moved.", 
                    parent=top
                )
            except Exception as e:
                msgbx.showerror(
                    title="Move Error", 
                    message=str(e), 
                    parent=top
                )
        next()

    def delete():
        """Delete the file."""
        try:
            delete_file(file_path)
            msgbx.showinfo(
                title="Success", 
                message=f"{os.path.basename(file_path)} deleted.", 
                parent=top
            )
        except Exception as e:
            msgbx.showerror(
                title="Delete Error", 
                message=str(e), 
                parent=top
            )
        next()

    ttk.Button(
        frame, 
        text='Cancel', 
        command=top.destroy
    ).grid(
        column=0, 
        row=0, 
        padx=5, 
        pady=5
    )
    ttk.Button(
        frame, 
        text="Leave", 
        command=next
    ).grid(
        column=1, 
        row=1, 
        padx=5, 
        pady=5
    )
    ttk.Button(
        frame, 
        text="Move", 
        command=move
    ).grid(
        column=2, 
        row=1, 
        padx=5, 
        pady=5
    )
    ttk.Button(
        frame, 
        text="Delete", 
        command=delete
    ).grid(
        column=3, 
        row=1, 
        padx=5, 
        pady=5
    )
