class Charger:
    def __init__(self, x_position, y_position):
        self.__position = (x_position, y_position)
        self.__direction = 0

    def turn(self):
        self.__direction += 1

        if self.__direction > 3:
            self.__direction = 0

    def render(self):
        if self.__direction == 0:
            return "u"

        if self.__direction == 1:
            return "l"

        if self.__direction == 2:
            return "d"

        if self.__direction == 3:
            return "r"

    def get_position(self):
        return self.__position

    def get_charge_zone(self):
        if self.__direction == 0:
            return tuple(map(sum, zip(self.__position, (1, 0))))

        if self.__direction == 1:
            return tuple(map(sum, zip(self.__position, (0, 1))))

        if self.__direction == 2:
            return tuple(map(sum, zip(self.__position, (-1, 0))))

        if self.__direction == 3:
            return tuple(map(sum, zip(self.__position, (0, -1))))

    def get_charge(self, cleaner):
        return 5