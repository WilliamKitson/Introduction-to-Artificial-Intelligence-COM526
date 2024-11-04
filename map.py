class Map:
    def __init__(self, data):
        substrings = str.splitlines(data)

        self.__width = len(substrings[0])
        self.__height = len(substrings)
        self.__data = [["" for i in range(self.__width)] for j in range(self.__height)]

        for i in range(self.__height):
            for j in range(self.__width):
                self.__data[i][j] = substrings[i][j]

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_blocked(self, x, y):
        return self.__data[x][y] == "x"

    def get_render(self, x, y):
        return self.__data[x][y]