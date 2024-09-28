import os


def get_directory_list():
    with open("./appReq/departments.txt") as file:
        directory_list_local = file.readlines()
        directory_list_local = [directory_local.strip() for directory_local in directory_list_local]
        return directory_list_local

show_dir = r"C:\Users\tanmay.maheshwari\Documents\server"
show_name = input("Enter the Show name: ")

show_types = ["commercial", "series","movie"]


serial_number = 1

for i in show_types:
    print(f"{serial_number}. {i.capitalize()}")
    serial_number += 1

show_type = input("Enter the show type: ")
show_dir = os.path.join(show_dir, show_name)
os.mkdir(show_dir)


print("These are the default directories for the show.")
serial_number = 1
for directory in get_directory_list():
    print(f"{serial_number}. {directory}")
    serial_number += 1

department_edit = input("Do you want to edit the department list(Yes/No): ")
department_edit = department_edit.lower()

if department_edit == "no":
    for department_name in get_directory_list():
        department_dir = os.path.join(show_dir, department_name)
        os.mkdir(department_dir)


# elif department_edit == "yes":
#     department_list_action = input("What do you want to do(Add/Remove/Edit/Complete): ")
#     if





