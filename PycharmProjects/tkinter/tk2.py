"""insert"""
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')

e = tk.Entry(window, show='*')
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)


def insert_1_2():
    var = e.get()
    t.insert(1.2, var)


b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', width=15, height=2, command=insert_point)
b2.pack()

b3 = tk.Button(window, text='insert 1_2', width=15, height=2, command=insert_1_2)
b3.pack()

t = tk.Text(window, height=2)
t.pack()
window.mainloop()

