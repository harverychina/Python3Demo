import xlrd

file = '/Python自动化办公实战/批量处理Excel/拆分与合并/a.xls'

data = xlrd.open_workbook(file)
table = data.sheets()[0]
value = table.cell_value(rowx=3, colx=3)
