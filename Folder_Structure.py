import os
from modules import functions
from modules import department_list_creator


show_dir = r"C:\Users\Tanmay\Documents\Shows"
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

department_edit_decision = input("Do you want to edit the Department Structure(Yes/No): ").lower()
department_edit_decision = department_edit_decision.strip()



if department_edit_decision == "yes":
    department_list_final = department_list_creator.department_list_editor()

else:
    department_list_final = functions.get_departments()

for department in department_list_final:
    if type(department) == str:
        department_dir = os.path.join(show_dir,department)
        os.mkdir(department_dir)

    else:
        department_dir = os.path.join(show_dir,list(department.keys())[0])
        os.mkdir(department_dir)
        for sub_folders in list(department.values())[0]:
            sub_folder_dir = os.path.join(department_dir,sub_folders)
            os.mkdir(sub_folder_dir)

