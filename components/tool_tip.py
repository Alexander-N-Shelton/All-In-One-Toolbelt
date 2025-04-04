# components/tool_tip.py

import tkinter as tk
from tkinter import ttk


class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")                  
        x = x + self.widget.winfo_rootx() + 20
        y = y + cy + self.widget.winfo_rooty() - 50
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y)) 

        label = ttk.Label(
            tw, 
            text=tip_text, 
            justify=tk.RIGHT,
            style="ToolTip.TLabel",
            relief=tk.SOLID,
            borderwidth=1, 
        )
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

def create_ToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        try: 
            toolTip.show_tip(text)
        except: 
            pass

    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)