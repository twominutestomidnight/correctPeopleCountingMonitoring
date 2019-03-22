from xlrd import open_workbook

def read_xml(file_name):
    book = open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    dict_list = []
    keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
    for row_index in range(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value
             for col_index in range(sheet.ncols)}
        dict_list.append(d)
    return dict_list