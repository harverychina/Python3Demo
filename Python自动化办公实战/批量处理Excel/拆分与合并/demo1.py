import xlrd

file = '/Users/huangjiancong/Desktop/Python3Demo/Python自动化办公实战/批量处理Excel/a.xls'

data = xlrd.open_workbook(file)
table = data.sheets()[0]
value = table.cell_value(rowx=3, colx=3)
