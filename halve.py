import os
import shutil
import random


os.chdir("./inputs/malaria_dataset/cell_images/validation")
path = os.getcwd()
folders = os.listdir()

for folder in folders:
    files = os.listdir(path + f"/{folder}")
    del_files = random.sample(files, len(files) // 2)
    os.remove(del_files)
