import os
import sys

directory = r"D:\Torrents\BCS"

for file in os.listdir(directory):
    if ".mkv" in file:
        title = file.replace(".mkv", "")
        command = r'mkvpropedit "{}\{}" --set "title={}"'.format(directory, file, title)
        os.system(command)
        print(title, " done")