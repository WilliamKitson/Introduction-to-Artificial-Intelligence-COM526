class Map:
    def __init__(self, data):
        substrings = str.splitlines(data)

        self.__width = len(substrings[0])
        self.__height = len(substrings)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height