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

department_creation_decision = input("Do you want to edit the Department Structure(Yes/No): ").lower()
department_creation_decision = department_creation_decision.strip()

if department_creation_decision == "yes":
    department_list_final = department_list_creator.department_list_editor()
    print(department_list_final)
else:
    print(functions.get_departments())

