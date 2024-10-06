import json


def get_departments(department_filepath = "appReq/departments.json"):
    with open(department_filepath) as file:
        departments_local = file.read()
        department_list_local = json.loads(departments_local)
        return department_list_local


def print_department_structure(department_list_local):
    for index,department in enumerate(department_list_local):

        if type(department) == dict:

            for department_name in department.keys():
                print(f"{index+1}.{department_name.capitalize()}")

            for department_parts in department.values():

                for serial,department_part_names in enumerate(department_parts):
                    print(f"  {serial+1}.{department_part_names}")

                print()


        elif type(department) == str:
            print(f"{index+1}.{department.capitalize()}\n")


        else:
            pass


def write_departments(department_list, path = ""):
    with open("appReq/departments_temp.json",'w') as file:
        file.write(department_list)


