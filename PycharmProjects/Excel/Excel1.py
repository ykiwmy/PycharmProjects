import xlrd
import xlwt
import struct
import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import *


readbook = xlrd.open_workbook('comcfg.xlsx')  # 打开文件
window = tk.Tk()
window.title('Sahara.bin生成工具')
# window.grid(column=0, row=0, sticky='nsew')
window.geometry('400x80')

var = tk.StringVar()
ttk.Label(window, text='站名').grid(column=0, row=0,ipadx=50, sticky='w')
ttk.Label(window, text='联锁ID').grid(column=1, row=0,ipadx=50, sticky='w')
ttk.Label(window, text='西门子ID').grid(column=2, row=0,ipadx=50, sticky='w')

window.name_entry = ttk.Entry(window, width=5)
window.name_entry.grid(column=0, row=1,sticky='w')
window.IxLID = ttk.Label(window, text='',)
window.IxLID.grid(column=1, row=1,sticky='w')
window.WCUID = ttk.Label(window, text='')
window.WCUID.grid(column=2, row=1,sticky='w')


# 通过名称获取sheet
def GetSheetByName(sheetname):
    return readbook.sheet_by_name(sheetname)

# 通过名称获取行数


def GetRowsByName(sheetname):
    sheet = GetSheetByName(sheetname)
    return sheet.nrows  # 获取sheet的行数

# 通过名称获取列数
def GetColsByName(sheetname):
    sheet = GetSheetByName(sheetname)
    return sheet.ncols  # 获取sheet的行数


# 获取自身站名
def GetSelfName(sheetname):
    sheet = GetSheetByName(sheetname)
    return sheet.cell(0, 1).value


def GetInfo(sheetname,selfname):
    nrows = GetRowsByName(sheetname)
    sheet = GetSheetByName(sheetname)
    IsFind = False
    IxL = 0xFF
    TGMT = 0xFF
    for i in range(1, nrows):
        name = sheet.cell(i, 0).value
        if name == selfname:
            IsFind = True
            IxL = sheet.cell(i, 1).value
            TGMT = sheet.cell(i, 2).value
    return (IsFind, int(IxL), int(TGMT))



def Generator():


tk.Button(window, text='Generator', command=Generator).grid(column=0, row=2,columnspan=3)

window.mainloop()


Info = GetInfo('Sahara', window.name_entry.get())
    if Info[0] is True:
        window.IxLID['text'] = Info[1]
        window.WCUID['text'] = Info[2]
        fp = open('Sahara.bin', 'wb')
        fp.write(struct.pack('BB', Info[1], Info[2]))
        showinfo(message='成功！')
        fp.close()
    else:
        showinfo(message='站名错误！')



