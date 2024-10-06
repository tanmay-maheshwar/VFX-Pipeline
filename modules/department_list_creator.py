if __name__ == "__main__":
    import functions
    PERMANENT_PATH = "../appReq/departments.json"
    TEMPORARY_PATH = "../appReq/departments_temp.json"

else:

    from modules import functions
    PERMANENT_PATH = "appReq/departments.json"
    TEMPORARY_PATH = "appReq/departments_temp.json"


def department_list_editor():

    department_list = str(functions.get_departments())
    department_list = department_list.replace("'",'"')

    functions.write_departments(department_list,TEMPORARY_PATH)

    while True:
        user_action = (input("Do you to 'add','show','remove',edit subfolders' or 'exit':")).lower()
        user_action = user_action.strip()

        if user_action.startswith('add'):
            department = user_action[4:]
            department = department.capitalize()

            additional_subfolders_decision = (input("Do you want to have sub-folders in this department(Yes/No): ")).lower()

            if additional_subfolders_decision == "yes":
                department_subfolder_list = []
                while True:
                    department_subfolders_name = input("Enter sub-folder name(One at a time): ")
                    department_subfolder_list.append(department_subfolders_name.capitalize())

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

            functions.write_departments(department_list_str, TEMPORARY_PATH)



        elif user_action.startswith('show'):
            department_list = functions.get_departments(TEMPORARY_PATH)
            functions.print_department_structure(department_list)


        elif user_action.startswith('remove'):

            try:
                department_list = functions.get_departments(TEMPORARY_PATH)

                remove_department = int(user_action.strip('remove '))
                department_list.pop(remove_department-1)
                department_list = str(department_list)
                department_list = department_list.replace("'",'"')

                functions.write_departments(department_list,TEMPORARY_PATH)


            except IndexError:
                print("Item is not in the list.")
                continue


        elif user_action.startswith('edit'):
            try:
                department_list = functions.get_departments(TEMPORARY_PATH)
                edit_department_serial = int(user_action.strip("edit "))

                new_subfolder_list = []

                while True:
                    edit_subfolders_name = input("Enter sub-folder name(One at a time): ")
                    new_subfolder_list.append(edit_subfolders_name.capitalize())

                    more_folder_decision = (input("Do you want to have more folders(Yes/No): ")).lower()

                    if more_folder_decision == "yes":
                        continue

                    else:
                        break

                if type(department_list[edit_department_serial - 1]) == str:


                    new_department_header = {department_list[edit_department_serial-1]: new_subfolder_list}
                    department_list[edit_department_serial-1] = new_department_header




                else:

                    head_folder_name = list(department_list[edit_department_serial-1].keys())[0]
                    new_department_header = {head_folder_name: new_subfolder_list}
                    department_list[edit_department_serial-1] = new_department_header



                department_list_str = str(department_list)
                department_list_str = department_list_str.replace("'", '"')

                functions.write_departments(department_list_str, TEMPORARY_PATH)


            except IndexError:


                print("Item not in list.")


        elif user_action == "exit":
            print("Happy Comping")

            break

        else:
            print("Enter a valid action.")



    return department_list
