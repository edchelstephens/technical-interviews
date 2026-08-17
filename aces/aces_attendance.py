from pprint import pprint
from collections import OrderedDict

from openpyxl import load_workbook

workbook = load_workbook("Aces_Attendance.xlsx")
sheet = workbook.active

data = []

for row in sheet.iter_rows(values_only=True):
    data.append(list(row))

pprint(data)
