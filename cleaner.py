class Cleaner:
    def __init__(self, x_position, y_position):
        self.__battery = 100
        self.__position = (x_position, y_position)

    def get_battery(self):
        return self.__battery

    def get_position(self):
        return self.__position