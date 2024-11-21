import json
import os
from itertools import count


# base_folder_name = "CG_New"


directory = r"T:\maha\REEL_02\RL_02_SH_0480\cg"
folders = ["Aura","AOVs","Particle"]
folder_name = ["RL_06_NIS_14"]


for shot in range(5):
    shot_dir = os.path.join(directory,f'Nandi_0{shot+1}')
    os.mkdir(shot_dir)

    for subfolder in folders:
        subfolder_dir = os.path.join(shot_dir,subfolder)
        os.mkdir(subfolder_dir)

#---------------------------------------------------------------------RENAMING FILES--------------------------------------------------------------------------------

#
# for file in os.listdir(directory):
#     new_name = file.split('.')[1]
#
#     if new_name.count('0') >= 3:
#         front_name = file.split('.')[0]
#         extension = file.split('.')[2]
#         frame_number =new_name.lstrip("0")
#         if len(frame_number) == 1:
#             new_digits = "000"+ frame_number
#         elif len(frame_number) == 2:
#             new_digits = "00"+ frame_number
#         else:
#             new_digits = "0"+frame_number
#         final_new_name = f'{front_name}.{new_digits}.{extension}'
#         print(final_new_name)
#         os.rename(os.path.join(directory,file),os.path.join(directory,final_new_name))

#----------------------------------------------------------------------FOLDER CREATOR BASED ON JASON---------------------------------------------------------------------


with open("departments.json") as file:
    department_str = file.read()

department_list_final = json.loads(department_str)


for shot in folder_name:
    shot_dir = os.path.join(directory,shot)
    os.mkdir(shot_dir)

    for department in department_list_final:
        if type(department) == str:
            department_dir = os.path.join(shot_dir,department)
            os.mkdir(department_dir)

        else:
            department_dir = os.path.join(shot_dir,list(department.keys())[0])
            os.mkdir(department_dir)

            for sub_folders in list(department.values())[0]:
                if type(sub_folders) == str:
                    sub_folder_dir = os.path.join(department_dir, sub_folders)
                    os.mkdir(sub_folder_dir)
                else:
                   sub_folder_dir = os.path.join(department_dir,list(sub_folders.keys())[0])
                   os.mkdir(sub_folder_dir)
                   for sub_sub_folder in list(sub_folders.values())[0]:
                       sub_sub_folder_dir = os.path.join(sub_folder_dir,sub_sub_folder)
                       os.mkdir(sub_sub_folder_dir)




#----------------------------------------------------------ONLY CG FOLDER CREATION--------------------------------------------------
# with open("cg_departments.json") as file:
#     department_str = file.read()
#
# department_list_final = json.loads(department_str)
#
#
#
# for department in department_list_final:
#     print(list(department.keys())[0])
#
#
#
#     department_dir = os.path.join(directory,list(department.keys())[0])
#     os.mkdir(department_dir)
#
#     for sub_folders in list(department.values())[0]:
#         if type(sub_folders) == str:
#             sub_folder_dir = os.path.join(department_dir, sub_folders)
#             os.mkdir(sub_folder_dir)
#         else:
#            sub_folder_dir = os.path.join(department_dir,list(sub_folders.keys())[0])
#            os.mkdir(sub_folder_dir)
#            for sub_sub_folder in list(sub_folders.values())[0]:
#                sub_sub_folder_dir = os.path.join(sub_folder_dir,sub_sub_folder)
#                os.mkdir(sub_sub_folder_dir)




#-------------------------------------------------------------------TESTING-------------------------------------------------------------------------------

