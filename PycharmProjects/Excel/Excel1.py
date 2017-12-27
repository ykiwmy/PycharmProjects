import xlrd
import xlwt
import struct


def GetSelfName():
    return
def read_excel(sheetname):
    readbook = xlrd.open_workbook('test.xlsx')  # 打开文件
    sheet = readbook.sheet_by_name(sheetname)  # 通过名称获取
    nrows = sheet.nrows  # 获取sheet的行数
    ncols = sheet.ncols  # 获取sheet的列数
    print(nrows, ncols)

    selfname = sheet.cell(0, 1).value
    print(selfname)
    for i in range(1,nrows):
        name = sheet.cell(i, 0).value
        IxL = sheet.cell(i, 1).value
        TGMT = sheet.cell(i, 2).value
        print(name, IxL, TGMT)


read_excel('Sheet1')
