import os
import sys


show_path = r'T:\maha'
thumbnail_folder = r'T:\maha\_ASSETS\thumnails'

for reel in os.listdir(show_path)[:1]:
    
    if reel == "_ASSETS":
        pass
    else:
        reel_path = os.path.join(show_path,reel)
        thumbnail_reel_folder = os.path.join(thumbnail_folder,reel)
        os.mkdir(thumbnail_reel_folder)

        for shot in os.listdir(reel_path)[:1]:
            
            
            shot_path = os.path.join(reel_path,shot,'scan')
            scan_folder_name = os.listdir(shot_path)[0]
            scan_path = os.path.join(shot_path,scan_folder_name)
            thumbnail_exr = os.listdir(scan_path)[0]
            thumbnail_exr_path = os.path.join(scan_path,thumbnail_exr)
            thumbnail_exr_path = thumbnail_exr_path.replace('\\',"//")
            thumbnail_name = f'{shot}_thumb.png'

            thumbnail_path = os.path.join(thumbnail_reel_folder,thumbnail_name)
            thumbnail_path = thumbnail_path.replace('\\',"//")

            
            shot_read = nuke.createNode('Read',inpanel = False)
            shot_read['file'].setValue(thumbnail_exr_path)
            
            reformate_node = nuke.createNode('Reformat',inpanel = False)
            reformate_node['format'].setValue('HD_1080')
            reformate_node['black_outside'].setValue(True)
            
            write_node = nuke.createNode('Write',inpanel = False)
            write_node['file'].setValue(thumbnail_path)
            write_node['file_type'].setValue('png')
            
            print(shot_read['first'].value())
            print(shot_read['last'].value())
            nuke.execute(write_node,int(shot_read['first'].value()),int(shot_read['last'].value()))


    





