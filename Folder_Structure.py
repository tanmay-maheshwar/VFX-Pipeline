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

department_creation_decision = input("Do you want to go with Default Department or want to edit the Department Structure(Yes/No): ").lower()
department_creation_decision = department_creation_decision.strip()

if department_creation_decision == "yes":

    while True:
        user_action = (input("Do you to 'add','show','remove',edit' or 'exit':")).lower()
        user_action = user_action.strip()


        if user_action.startswith('add'):
            department = user_action[4:]
            department = department.capitalize()


            department_list = functions.get_departments()

            department_list.appen

            write_todos(todo_List)


        elif user_action.startswith('show'):

            todo_List = get_todos()

            todo_new_list = [item.strip('\n') for item in todo_List]
            todo_List = todo_new_list


            for index,x in enumerate(todo_List):
                print(f"{index + 1}. {x.capitalize()}")


        elif user_action.startswith('complete'):

            try:
                todo_List = get_todos()

                completed_task = int(user_action.strip('complete '))
                completed_task_value = todo_List[completed_task - 1].replace('\n','')
                print(f'{completed_task_value.capitalize()} has been marked completed.')
                todo_List.pop(completed_task-1)

                write_todos(todo_List)

            except IndexError:
                print("Item is not in the list.")
                continue


        elif user_action.startswith('edit'):
            try:
                todo_List = get_todos()

                edited_task = int(user_action[5:])
                edited_task_value = todo_List[edited_task - 1].replace('\n','')
                new_task = input("Enter the new task:")

                print(f'{edited_task_value.capitalize()} has been changed to {new_task.capitalize()}.')
                todo_List[edited_task- 1] = new_task.capitalize() + '\n'

                write_todos(todo_List)


            except ValueError:
                print("Your command is invalid.")
                continue

        elif user_action.startswith("exit"):
            break


        else:
            print("Invalid command!")


    print("Happy Comping!")
