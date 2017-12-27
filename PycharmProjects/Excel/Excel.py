import xlrd
import xlwt
# 打开一个excel文件得到数据
readbook = xlrd.open_workbook('./Excel/test.xlsx')
# 获取一个表格数据
sheet = readbook.sheets()[0]            #通过索引获取
sheet = readbook.sheet_by_index(0)#索引的方式，从0开始
sheet = readbook.sheet_by_name('Sheet1')#名字的方式
#获取sheet的最大行数和列数
nrows = sheet.nrows#行
ncols = sheet.ncols#列
print(nrows,ncols)
# 获取某个单元格的值
list = []
for i in range(0, nrows):
    for j in range(0, ncols):
        print(sheet.cell(i,j).value)
# 打开将写的表并添加sheet
# writebook = xlwt.Workbook()#打开一个excel
# sheet = writebook.add_sheet('test')#在打开的excel中添加一个sheet
# # 获取表格数据
# nrows = table.nrows                 #行数
# ncols = table.ncols                 #列数
# data = table.cell(nrow, ncol).value #得到表格数据
# #获取每行每列的数据
# for i in range(0, nrows):
#     for j in range(0, ncols):
#         data = table.cell(i, j).value