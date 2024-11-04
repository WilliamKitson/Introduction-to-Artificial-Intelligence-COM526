from version1 import Version1

def load_map(filepath):
    with open(filepath, 'r') as file:
        file_content = file.read()

    return file_content

Version1(load_map("maps/simple_map.txt")).execute()