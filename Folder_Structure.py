import os
from modules import functions


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
department_list = functions.get_departments()
functions.print_department_structure(department_list)

department_edit = input("Do you want to edit the department list(Yes/No): ")
department_edit = department_edit.lower()

if department_edit == "no":
    for department_name in get_directory_list():
        department_dir = os.path.join(show_dir, department_name)
        os.mkdir(department_dir)


elif department_edit == "yes":
    department_list = functions.get_departments()


    #THIS PRINTS ALL DEPARTMENTS
    for index, department in enumerate(department_list):

        if type(department) == dict:

            for department_name in department.keys():
                print(f"{index + 1}.{department_name.capitalize()}")

            for department_parts in department.values():

                for serial, department_part_names in enumerate(department_parts):
                    print(f"  {serial + 1}.{department_part_names}")

                print()


        elif type(department) == str:
            print(f"{index + 1}.{department.capitalize()}\n")


        else:
            pass

#     department_list_action = input("What do you want to do(Add/Remove/Edit/Complete): ")
#     if





