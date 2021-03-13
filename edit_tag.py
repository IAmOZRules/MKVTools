import os
import sys

directory = r"D:\Torrents\Breaking Bad"

for file in os.listdir(directory):
    if ".mkv" in file:
        title = file.replace(".mkv", "")
        command = r'mkvpropedit "D:\Torrents\Breaking Bad\{}" --set "title={}"'.format(file, title)
        os.system(command)
        print(title, " done")