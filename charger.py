class Charger:
    def __init__(self, x_position, y_position):
        self.__position = (x_position, y_position)
        self.__direction = 0

    def turn(self):
        self.__direction += 1

        if self.__direction > 3:
            self.__direction = 0

    def __facing_north(self):
        return self.__direction == 0

    def __facing_east(self):
        return self.__direction == 1

    def __facing_south(self):
        return self.__direction == 2

    def __facing_west(self):
        return self.__direction == 3

    def get_position(self):
        return self.__position

    def get_charge_zone(self):
        if self.__facing_north():
            return tuple(map(sum, zip(self.__position, (1, 0))))

        if self.__facing_east():
            return tuple(map(sum, zip(self.__position, (0, 1))))

        if self.__facing_south():
            return tuple(map(sum, zip(self.__position, (-1, 0))))

        if self.__facing_west():
            return tuple(map(sum, zip(self.__position, (0, -1))))

    def get_charge(self, cleaner):
        if cleaner == self.get_charge_zone():
            return 5

        return 0

    def get_render(self):
        if self.__facing_north():
            return "u"

        if self.__facing_east():
            return "l"

        if self.__facing_south():
            return "d"

        if self.__facing_west():
            return "r"