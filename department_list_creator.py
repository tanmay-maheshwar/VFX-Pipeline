from modules import functions


department_creation_decision = input("Do you want to edit the Department Structure(Yes/No): ").lower()
department_creation_decision = department_creation_decision.strip()


if department_creation_decision == "yes":

    department_list = str(functions.get_departments())
    department_list = department_list.replace("'",'"')

    functions.write_departments(department_list)

    while True:
        user_action = (input("Do you to 'add','show','remove',edit' or 'exit':")).lower()
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
            department_list.append(department)
            department_list_str = str(department_list)
            department_list_str = department_list_str.replace("'",'"')



            with open("appReq/departments_temp.json",'w') as file:
                file.write(department_list_str)



        elif user_action.startswith('show'):
            department_list = functions.get_departments("appReq/departments_temp.json")
            functions.print_department_structure(department_list)


        elif user_action.startswith('remove'):

            try:
                department_list = functions.get_departments("appReq/departments_temp.json")

                remove_department = int(user_action.strip('remove '))
                department_list.pop(remove_department-1)
                department_list = str(department_list)
                department_list = department_list.replace("'",'"')

                functions.write_departments(department_list)


            except IndexError:
                print("Item is not in the list.")
                continue


        elif user_action.startswith('edit'):
            try:
                department_list = functions.get_departments()
                edit_department_serial = int(user_action.strip("edit "))

                if type(department_list[edit_department_serial - 1]) == str:
                    new_department_name = input("Enter the new department name: ")

                    department_list[edit_department_serial - 1] = new_department_name

                else:

                    edit_action = input("Do you want to edit the Head or Sub folder: ").lower()
                    





            except ValueError:
                print("Your command is invalid.")
                continue
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
