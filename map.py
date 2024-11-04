class Map:
    def __init__(self, data):
        substrings = str.splitlines(data)
        width = len(substrings[0])
        height = len(substrings)

        self.__data = [["" for i in range(width)] for j in range(height)]

        for i in range(height):
            for j in range(width):
                self.__data[i][j] = substrings[i][j]

    def get_width(self):
        return len(self.__data[0])

    def get_height(self):
        return len(self.__data)

    def get_blocked(self, x, y):
        return self.__data[x][y] == "x"