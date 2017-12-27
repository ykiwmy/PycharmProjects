import xlrd
import xlwt
import struct


readbook = xlrd.open_workbook('test.xlsx')  # 打开文件

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
    for i in range(1,nrows):
        name = sheet.cell(i, 0).value
        if name == selfname:
            IxL = sheet.cell(i, 1).value
            TGMT = sheet.cell(i, 2).value
            #print(name, IxL, TGMT)
            return(name,IxL,TGMT)

SelfName = GetSelfName('SelfInfo')
print(SelfName)
Info = GetInfo('Sahara',SelfName)


