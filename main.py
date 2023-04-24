import os
import re


def sort_jpg():
    name = input("Name of your folder: ")
    directory = input("Path to your folder: ")
    old_folder = directory+"/"+name
    raw_folder = directory+"/"+name+"/RAW"
    #creating new folder
    if not os.path.exists(raw_folder):
        os.makedirs(raw_folder)
    #iterating over files
    for file in os.listdir(old_folder):
        if re.search("NEF", file):
            os.rename(old_folder+"/"+file, raw_folder+"/"+file)


if __name__ == "__main__":
    sort_jpg()
