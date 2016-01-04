import os
import string

path = "/Users/somash/Downloads/prank"
file_list = os.listdir(path)
print("Current Working Directory: " + os.getcwd())
os.chdir(path)
print("Changed the current working directory to: " + path)
for file_name in file_list:
    filtered_name = ''.join(filter(lambda x: not x.isdigit(), file_name))
    os.rename(file_name, filtered_name)
