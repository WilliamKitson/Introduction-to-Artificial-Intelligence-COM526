class Cleaner:
    def __init__(self, x_position, y_position):
        self.__battery = 100
        self.__position = (x_position, y_position)
        self.__forwards = 0

    def cycle(self):
        if self.__forwards == 0:
            self.__battery -= 1

        if self.__forwards == 1:
            self.__battery -= 2
            self.__position = (self.get_position()[0] + 1, self.get_position()[1])

    def get_battery(self):
        return self.__battery

    def get_position(self):
        return self.__position

    def set_forwards(self, forwards):
        self.__forwards = forwards