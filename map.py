import random

class Map:
    def __init__(self, data):
        substrings = str.splitlines(data)

        self.__width = len(substrings[0])
        self.__height = len(substrings)
        self.__data = [["" for i in range(self.__width)] for j in range(self.__height)]
        self.__randomise_dirt(substrings)

    def __randomise_dirt(self, substrings):
        for i in range(self.__height):
            for j in range(self.__width):
                character = substrings[i][j]

                if substrings[i][j] == " ":
                    character = str(random.randrange(0, 3))

                self.__data[i][j] = character

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_start(self):
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__data[i][j] == "^":
                    return i, j

    def get_charger(self):
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__data[i][j] == "u":
                    return i, j

    def get_blocked(self, position):
        if self.__data[position[0]][position[1]] in ["x", "u"]:
            return 0

        return 1

    def get_dirt(self, position):
        if self.__data[position[0]][position[1]] in ["x", "^", "u"]:
            return 0

        return int(self.__data[position[0]][position[1]])

    def get_render(self, position):
        output = self.__data[position[0]][position[1]]

        if output == "x":
            return output

        return " "