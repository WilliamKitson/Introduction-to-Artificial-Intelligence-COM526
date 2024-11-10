class Charger:
    def __init__(self, x_position, y_position):
        self.__direction = 0

    def turn(self):
        self.__direction = 1

    def render(self):
        if self.__direction == 0:
            return "u"

        if self.__direction == 1:
            return "i"