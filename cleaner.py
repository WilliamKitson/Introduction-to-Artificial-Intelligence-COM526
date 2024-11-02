class Cleaner:
    def __init__(self, x_position, y_position):
        self.__cycle = 0
        self.__battery = 100
        self.__position = (x_position, y_position)
        self.__forwards = 0
        self.__direction = 0

    def cycle(self):
        self.__cycle += 1

        match self.__forwards:
            case 0:
                self.__battery -= 1
                self.__process_direction()

            case 1:
                self.__battery -= 2

                match self.__direction:
                    case 0:
                        self.__move_north()

                    case 1:
                        self.__move_east()

                    case 2:
                        self.__position = (self.get_position()[0] - 1, self.get_position()[1])

                    case 3:
                        self.__position = (self.get_position()[0], self.get_position()[1] - 1)

    def __process_direction(self):
        self.__direction += 1

        if self.__direction == 4:
            self.__direction = 0

    def __move_north(self):
        self.__position = (
            self.get_position()[0] + 1,
            self.get_position()[1]
        )

    def __move_east(self):
        self.__position = (
            self.get_position()[0],
            self.get_position()[1] + 1
        )

    def get_cycle(self):
        return self.__cycle

    def get_battery(self):
        return self.__battery

    def get_position(self):
        return self.__position

    def get_render(self):
        match self.__direction:
            case 0:
                return "^"

            case 1:
                return ">"

            case 2:
                return "v"

            case 3:
                return "<"

    def set_forwards(self, forwards):
        self.__forwards = forwards