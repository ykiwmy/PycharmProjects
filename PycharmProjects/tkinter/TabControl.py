import tkinter as tk  # imports
from tkinter import ttk


win = tk.Tk()  # Create instance
win.title("ATP_SIM")  # Add a title
win.geometry('500x300')

tabControl = ttk.Notebook(win)  # Create Tab Control
tabControl.pack(expand=0, fill="both")  # Pack to make visible
tab_signal = ttk.Frame(tabControl)  # Create a tab
tabControl.add(tab_signal, text='信号机')  # Add the tab


monty = ttk.LabelFrame(tab_signal, text='名称')
monty.grid(column=0, row=0)
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')


tab_ts = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab_ts, text='Ts')  # Make second tab visible
win.mainloop()  # Start GUI

