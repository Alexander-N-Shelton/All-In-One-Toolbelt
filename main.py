# toolbelt/main.py

import tkinter as tk
from tkinter import ttk
from ui.date_calculator import DateCalculatorTab
from ui.file_manager import FileManagerTab

class ToolBelt(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('All-In-One Toolbelt')
        self.geometry('800x800')

        self.style = ttk.Style()

        self.style.theme_use('clam')

        self.tabControl = ttk.Notebook(self)

        self.date_tab = DateCalculatorTab(self.tabControl)
        self.file_tab = FileManagerTab(self.tabControl)

        self.tabControl.add(self.date_tab, text=' - Date Calculator -')
        self.tabControl.add(self.file_tab, text='- File Manager -')

        self.tabControl.pack(expand=1, fill='both')


if __name__ == "__main__":
    app = ToolBelt()
    app.mainloop()
