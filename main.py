from version1 import Version1

with open("maps/simple_map.txt", 'r') as file:
    file_content = file.read()

Version1(file_content).execute()