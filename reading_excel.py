from xlrd import open_workbook
import xlwt
dict_list = []
book = open_workbook('test.xls')
sheet = book.sheet_by_index(0)
book1= open_workbook('test1.xls')
sheet1=book.sheet_by_index(0)
keys = sheet.row_values(0)
values = [sheet1.row_values(i) for i in range(1, sheet1.nrows)]
sheets = ["Sheet 1"]

wb = xlwt.Workbook()
file_name = "output.xls"
for sheet, data in zip(sheets, [values]):
    # print sheet,data
    ws = wb.add_sheet(sheet)
    for row, row_value in enumerate(data):
        # print row,row_value
        for col, col_value in enumerate(row_value):
            # print col_value,col
            ws.write(row, col, col_value)

wb.save(file_name)