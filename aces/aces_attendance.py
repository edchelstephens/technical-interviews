from pprint import pprint

from openpyxl import load_workbook, Workbook

workbook = load_workbook("Aces_Attendance.xlsx")
sheet = workbook.active

data = []

for index, row in enumerate(sheet.iter_rows(values_only=True)):
    if index == 0:
        continue
    data.append(list(row))


cleaned_data = []

for data_list in data:
    player_name_list = [name for name in data_list if name is not None]
    cleaned_data.extend(player_name_list)

processed_data = [name.lower() for name in cleaned_data]
processed_data.sort()

attendance_dict = dict()

for name in processed_data:
    if name in attendance_dict:
        attendance_dict[name] += 1
    else:
        attendance_dict[name] = 1

print(" ===== Attendance Dict ====== ")
pprint(attendance_dict)


output_workbook = Workbook()
sheet = output_workbook.active

sheet.title = "Aces_Attendance_Count"
sheet.append(["Name", "Attendance"])

for name, count in attendance_dict.items():
    sheet.append([name, count])

output_workbook.save("Aces_Attendance_count.xlsx")

with open("attendance_dict.py", "w") as attendance_json:
    attendance_json.write(str(attendance_dict))
