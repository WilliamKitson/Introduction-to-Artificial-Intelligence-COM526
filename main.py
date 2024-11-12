from version1 import Version1

with open("COM526_map.txt", 'r') as file:
    file_content = file.read()

Version1(file_content).execute()