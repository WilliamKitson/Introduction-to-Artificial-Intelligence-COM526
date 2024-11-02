class Cleaner:
    def __init__(self, x_position, y_position):
        self.__cycle = 0
        self.__battery = 100
        self.__position = (x_position, y_position)
        self.__forwards = 0
        self.__direction = 0

    def cycle(self):
        self.__increment_cycle()
        self.__process_turn()
        self.__process_move()

    def __increment_cycle(self):
        self.__cycle += 1

    def __process_turn(self):
        if self.__path_blocked():
            self.__process_battery(1)
            self.__process_direction()

    def __path_blocked(self):
        return self.__forwards == 0

    def __process_battery(self, cost):
        self.__battery -= cost

        if self.__battery < 0:
            self.__battery = 0

    def __process_direction(self):
        self.__direction += 1

        if self.__direction == 4:
            self.__direction = 0

    def __process_move(self):
        if not self.__path_blocked():
            self.__process_battery(2)
            self.__move_north()
            self.__move_east()
            self.__move_south()
            self.__move_west()

    def __move_north(self):
        if self.__facing_north():
            self.__position = (
                self.get_position()[0] + 1,
                self.get_position()[1]
            )

    def __facing_north(self):
        return self.__direction == 0

    def __move_east(self):
        if self.__facing_east():
            self.__position = (
                self.get_position()[0],
                self.get_position()[1] + 1
            )

    def __facing_east(self):
        return self.__direction == 1

    def __move_south(self):
        if self.__facing_south():
            self.__position = (
                self.get_position()[0] - 1,
                self.get_position()[1]
            )

    def __facing_south(self):
        return self.__direction == 2

    def __move_west(self):
        if self.__facing_west():
            self.__position = (
                self.get_position()[0],
                self.get_position()[1] - 1
            )

    def __facing_west(self):
        return self.__direction == 3

    def get_cycle(self):
        return self.__cycle

    def get_battery(self):
        return self.__battery

    def get_position(self):
        return self.__position

    def get_render(self):
        if self.__facing_north():
            return "^"

        if self.__facing_east():
            return ">"

        if self.__facing_south():
            return "v"

        if self.__facing_west():
            return "<"

    def set_forwards(self, forwards):
        self.__forwards = forwards