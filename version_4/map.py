#  Copyright (c) 2024. William E. Kitson

import random
import json

class Map:
    def __init__(self, map_data, readings_filepath):
        self.__map_data = []
        self.__load_map(map_data)
        self.__geometry_data = []
        self.__load_geometry(readings_filepath)

    def __load_map(self, map_data):
        for row in iter(map_data.splitlines()):
            randomised_row = ""

            for character in row:
                randomised_row += character.replace(" ", str(random.randrange(0, 9)))

            self.__map_data.append(randomised_row)

    def __load_geometry(self, readings_filepath):
        try:
            with open(readings_filepath, 'r') as file:
                readings_data = json.load(file)

            for i in readings_data:
                self.__geometry_data.append((
                    i,
                    readings_data[i]
                ))

        except FileNotFoundError:
            return

    def get_width(self):
        return len(self.__map_data[0])

    def get_height(self):
        return len(self.__map_data)

    def get_start(self):
        return self.__get_character_coordinates("^")

    def __get_character_coordinates(self, character):
        for y, row in enumerate(self.__map_data):
            for x, column in enumerate(row):
                if column == character:
                    return x, y

    def get_charger(self):
        return self.__get_character_coordinates("u")

    def get_blocked(self, position):
        return int(self.__map_data[position[1]][position[0]] not in ["x", "u"])

    def get_dirt(self, position):
        dirt = self.__map_data[position[1]][position[0]]

        if dirt in ["x", "^", "u"]:
            return 0

        try:
            return float(dirt)

        except ValueError:
            return 0

    def get_render(self, position):
        render = self.__map_data[position[1]][position[0]]

        if render == "x":
            return render

        return " "

    def set_dirt(self, position, cleaned):
        row = self.__map_data[position[1]]
        new_row = ""

        for i in range(len(row)):
            if i == position[0]:
                new_row += str(cleaned)

            else:
                new_row += row[i]

        self.__map_data[position[1]] = new_row

    def set_geometry(self, position, geometry):
        self.__geometry_data.append((position, geometry))

    def get_geometry(self, position):
        for i in self.__geometry_data:
            if i[0] == str(position):
                return i[1]