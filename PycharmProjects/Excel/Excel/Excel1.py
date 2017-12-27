import xlrd
import xlwt

def read_excel():
  # 打开文件
    readbook = xlrd.open_workbook(r'E:\代码\PycharmProjects\PycharmProjects\PycharmProjects\Excel\Excel\test.xlsx')
    writebook = xlwt.Workbook()#打开一个excel
    sheet = writebook.add_sheet('test')#在打开的excel中添加一个sheet
    table = readbook.sheets()[0]#获取读入的文件的第一个sheet
    nrows = table.nrows#获取sheet的行数
    ncols = table.ncols#获取sheet的列数
    print (nrows,ncols)
    for i in range(nrows):
        if i == 0 or i == 1:  # 我处理的数据第一行是属性名，所以去掉
            continue
        for j in range(ncols):
            lng = table.cell(i,j).value#获取i行3列的表格值
            sheet.write(i-2,j,lng)#写入excel
    writebook.save('answer.xls')#一定要记得保存

read_excel()