
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

inLoop = False
while inLoop == False: 
    option = input("is your file a xls or a csv file ? (xls or csv) ")

    if option == "xls" or option == "csv":
        inLoop = True
        excelFile = xlrd.open_workbook("employeedata.{}".format(option))
        sheet = excelFile.sheet_by_index(0)
        writeFile = open_workbook("employeedata.{}".format(option))
        copiedFile = copy(writeFile)
        saver = copiedFile.get_sheet(0)
        for rx in range(sheet.nrows - 1):
            replacer = sheet.cell_value(rowx=rx + 1, colx=1)
            replacer = replacer.replace("handsinhands.org", "helpinghands.com")
            saver.write(rx + 1, 1, replacer)
        copiedFile.save('employeedata.{}'.format(option))
    else:
        print("please enter a valid option")