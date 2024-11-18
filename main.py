from version_1.demonstration import Demonstration

with open("maps/COM526_map_simple.txt", 'r') as file:
    file_content = file.read()

Demonstration(file_content).execute()