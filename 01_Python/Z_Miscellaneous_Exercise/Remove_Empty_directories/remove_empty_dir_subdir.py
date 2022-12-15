import os

root_dir = "C:\\Users\\Prince\\Desktop\\folder"

for dir_path, dir_names, file_names in os.walk(root_dir):
    if not os.listdir(dir_path):
        os.rmdir(dir_path)

