# toolbelt/ui/date_calculator.py

import tkinter as tk
from tkinter import ttk, messagebox as msgbx
from datetime import datetime
from logic.date_utils import calculate_date
from components.tool_tip import create_ToolTip

class DateCalculatorTab(ttk.Frame):
    """
    Date Calculator Tab. 
    Calculates the date given a specific amount of time
    """
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_opts = {'padx': 10, 'pady': 10}
        self._build_ui()

    def _build_ui(self):
        date_frame = ttk.LabelFrame(
            self, 
            text='Date Calculator', 
            borderwidth=10, 
            labelanchor='n'
        )
        date_frame.grid(
            column=0, 
            row=0, 
            sticky='W', 
            **self.grid_opts
        )

        # Static Labels
        ttk.Label(
            date_frame, 
            text='Months'
        ).grid(
            column=0, 
            row=1, 
            sticky='W', 
            **self.grid_opts
        )
        ttk.Label(
            date_frame, 
            text='Days'
        ).grid(
            column=1, 
            row=1, 
            sticky='W', 
            **self.grid_opts
        )
        ttk.Label(
            date_frame, 
            text='Years'
        ).grid(
            column=2, 
            row=1, 
            sticky='W', 
            **self.grid_opts
        )

        today = datetime.now()
        today_month, today_day, today_year = today.month, today.day, today.year

        # Date Inputs
        self.month_var = tk.IntVar(value=today_month)
        self.day_var = tk.IntVar(value=today_day)
        self.year_var = tk.IntVar(value=today_year)

        ttk.Spinbox(
            date_frame, 
            from_=1, 
            to=12, 
            textvariable=self.month_var, 
            font=(
                'Hack', 14
            ),
            width=5,
            state="readonly"
        ).grid(
            column=0, 
            row=2, 
            sticky='W', 
            **self.grid_opts
        )
        ttk.Spinbox(
            date_frame, 
            from_=1, 
            to=31, 
            textvariable=self.day_var, 
            font=(
                'Hack', 14
            ),
            width=5,
            state="readonly"
        ).grid(
            column=1, 
            row=2, 
            sticky='W', 
            **self.grid_opts
        )
        ttk.Spinbox(
            date_frame, 
            from_=1990, 
            to=2100, 
            textvariable=self.year_var, 
            font=(
                'Hack', 14
            ),
            width=8,
            state="readonly"
        ).grid(
            column=2, 
            row=2, 
            sticky='W', 
            **self.grid_opts
        )

        # Time period input
        self.time_period = tk.StringVar()
        self.time_period_entry = ttk.Entry(
            date_frame, 
            textvariable=self.time_period,
            font=(
                'Hack', 14
            ),
            width=10,
        )
        self.time_period_entry.grid(
            column=3, 
            row=2, 
            sticky='W', 
            **self.grid_opts
        )
        create_ToolTip(self.time_period_entry, text='Enter a Number')
        self.time_period_entry.focus()

        # Time unit radio buttons
        self.time_unit = tk.StringVar(value='Days')
        units = ['Days', 'Weeks', 'Months', 'Years']
        for idx, label in enumerate(units):
            ttk.Radiobutton(
                date_frame,
                text=label,
                variable=self.time_unit,
                value=label
            ).grid(column=idx, row=3, sticky='W', **self.grid_opts)


        # Calculate button
        ttk.Button(
            date_frame, 
            text='Calculate', 
            command=self.on_calculate,
            style='Large.TButton',
        ).grid(
            column=0, 
            row=4, 
            columnspan=4, 
            sticky='S', 
            **self.grid_opts
        )

    def on_calculate(self):
        try:
            start = datetime(
                year=self.year_var.get(),
                month=self.month_var.get(),
                day=self.day_var.get()
            )
            period = int(self.time_period.get())
            unit = self.time_unit.get()

            new_date = calculate_date(start, period, unit)

            msgbx.showinfo(
                "Calculation Result",
                f"{period} {unit} from {start.strftime('%m/%d/%Y')} is:\n{new_date.strftime('%m/%d/%Y')}"
            )
        except Exception as e:
            msgbx.showerror(
                'Invalid Input', 
                'Please enter a valid number.'
            )
