from modules import functions

department_creation_decision = input("Do you want to go with Default Department or want to edit the Department Structure(Yes/No): ").lower()
department_creation_decision = department_creation_decision.strip()

if department_creation_decision == "yes":

    while True:
        user_action = (input("Do you to 'add','show','complete',edit' or 'exit':")).lower()
        user_action = user_action.strip()


        if user_action.startswith('add'):
            department = user_action[4:]
            department = department.capitalize()


            additional_subfolders_decision = (input("Do you want to have sub-folders in this department(Yes/No): ")).lower()

            if additional_subfolders_decision == "yes":
                department_subfolder_list = []
                while True:
                    department_subfolders_name = input("Enter sub-folder name(One at a time): ")
                    department_subfolder_list.append(department_subfolders_name)

                    more_folder_decision = (input("Do you want to have more folders(Yes/No): ")).lower()

                    if more_folder_decision == "yes":
                        continue

                    else:
                        break

                department = {department:department_subfolder_list}

            else:
                pass

            department_list = functions.get_departments()
            print(department_list)
            department_list.append(department)
            print(department_list)
            department_list_str = str(department_list)



            with open("appReq/departments_temp.json",'w') as file:
                file.write(department_list_str)



        elif user_action.startswith('show'):
            department_list = functions.get_departments()
            functions.print_department_structure(department_list)

        #WAS FIGURING OUT JSON WRITING
    #
    #
    #     elif user_action.startswith('complete'):
    #
    #         try:
    #             todo_List = get_todos()
    #
    #             completed_task = int(user_action.strip('complete '))
    #             completed_task_value = todo_List[completed_task - 1].replace('\n','')
    #             print(f'{completed_task_value.capitalize()} has been marked completed.')
    #             todo_List.pop(completed_task-1)
    #
    #             write_todos(todo_List)
    #
    #         except IndexError:
    #             print("Item is not in the list.")
    #             continue
    #
    #
    #     elif user_action.startswith('edit'):
    #         try:
    #             todo_List = get_todos()
    #
    #             edited_task = int(user_action[5:])
    #             edited_task_value = todo_List[edited_task - 1].replace('\n','')
    #             new_task = input("Enter the new task:")
    #
    #             print(f'{edited_task_value.capitalize()} has been changed to {new_task.capitalize()}.')
    #             todo_List[edited_task- 1] = new_task.capitalize() + '\n'
    #
    #             write_todos(todo_List)
    #
    #
    #         except ValueError:
    #             print("Your command is invalid.")
    #             continue
    #
    #     elif user_action.startswith("exit"):
    #         break
    #
    #
    #     else:
    #         print("Invalid command!")
    #
    #
    # print("Happy Comping!")
    #
