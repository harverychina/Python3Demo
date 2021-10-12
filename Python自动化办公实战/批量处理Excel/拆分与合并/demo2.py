import xlwt

dst_file = "/Python自动化办公实战/批量处理Excel/拆分与合并/b.xls"

workbook = xlwt.Workbook(encoding='utf-8')
xlsheet = workbook.add_sheet("统计结果")

xlsheet.write(0, 0, "统计结果")
xlsheet.write(0, 1, "学习强国")

workbook.save(dst_file)
