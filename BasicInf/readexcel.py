import openpyxl


def writeExcel(i, ain, bin, cin, din, ein):
    wb = openpyxl.load_workbook('文件地址')
    sheet = wb['Sheet页名称']
    sheet.append([i, ain, bin, cin, din, ein])
    wb.save('文件地址')
