import tkinter
from tkinter import ttk


class AddWidget(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        quit()

    def add_two_num(self):
        num1 = int(self.num1_entry.get())
        num2 = int(self.num2_entry.get())
        num3 = num1 + num2
        self.answer_label['text'] = num3

    def init_gui(self):
        self.root.title('两数相加')
        self.root.option_add('*tearOff', 'FALSE')

        self.grid(column=0, row=0, sticky='nsew')

        self.menubar = tkinter.Menu(self.root)
        self.menu_file = tkinter.Menu(self.menubar)
        self.menu_file.add_command(label='退出', command=self.on_quit)

        self.menu_edit = tkinter.Menu(self.menubar)

        self.menubar.add_cascade(menu=self.menu_file, label='文件')
        self.menubar.add_cascade(menu=self.menu_edit, label='退出')

        self.root.config(menu=self.menubar)

        self.num1_entry = ttk.Entry(self, width=5)
        self.num1_entry.grid(column=1, row=2)

        self.num2_entry = ttk.Entry(self, width=5)
        self.num2_entry.grid(column=3, row=2)

        self.calc_button = ttk.Button(self, text='计算',
                                      command=self.add_two_num)
        self.calc_button.grid(column=0, row=3, columnspan=4)

        self.answer_frame = ttk.LabelFrame(self, text='结果',
                                           height=100)
        self.answer_frame.grid(column=0, row=4, columnspan=4, sticky='nesw')

        self.answer_label = ttk.Label(self.answer_frame, text='')
        self.answer_label.grid(column=0, row=0)

        ttk.Label(self, text='两个数').grid(column=0, row=0,
                                         columnspan=4)
        ttk.Label(self, text='第一个数').grid(column=0, row=2,
                                          sticky='w')
        ttk.Label(self, text='第二个数').grid(column=2, row=2,
                                          sticky='w')

        ttk.Separator(self, orient='horizontal').grid(column=0,
                                                      row=1, columnspan=4, sticky='ew')


if __name__ == '__main__':
    mainFrame = tkinter.Tk()

    AddWidget(mainFrame)

    mainFrame.mainloop()

