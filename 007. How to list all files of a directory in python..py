# 007. How to list all files of a directory in python.
from os import listdir
from os.path import isfile, join

file_list = [f for f in listdir("/Users") if isfile(join("/Users", f))]
print(file_list)