"""canvas"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(window, bg='black', height=200, width=200)
canvas.pack()

x0, y0, x1, y1 = 50,  50,  80,  80
line = canvas.create_line(x0, y0, x1, y1)

window.mainloop()

