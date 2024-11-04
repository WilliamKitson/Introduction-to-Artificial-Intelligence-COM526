from version1 import Version1

def load_map():
    with open("map_data.txt", 'r') as file:
        file_content = file.read()

    return file_content

Version1(load_map()).execute()