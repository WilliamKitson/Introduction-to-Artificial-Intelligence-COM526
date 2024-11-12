class Cleaner:
    def __init__(self, position):
        self.__cycle = 0
        self.__battery = 100
        self.__position = position
        self.__dirt = 0
        self.__scan = 0
        self.__direction = 0

    def sense(self, dirt, forwards_scan):
        self.__dirt = dirt
        self.__scan = forwards_scan

    def cycle(self):
        self.__increment_cycle()

        if self.__dirt > 0:
            self.__process_battery(3)
            return

        self.__process_turn()
        self.__process_move()

    def __increment_cycle(self):
        self.__cycle += 1

    def __process_turn(self):
        if self.__battery_empty():
            return

        if not self.__path_blocked():
            return

        self.__process_battery(1)
        self.__process_direction()

    def __battery_empty(self):
        return self.__battery == 0

    def __path_blocked(self):
        return self.__scan == 0

    def __process_battery(self, cost):
        self.__battery -= cost

        if self.__battery < 0:
            self.__battery = 0

    def __process_direction(self):
        self.__direction += 1

        if self.__direction == 4:
            self.__direction = 0

    def __process_move(self):
        if self.__battery_empty():
            return

        if self.__path_blocked():
            return

        self.__process_battery(2)
        self.__move_north()
        self.__move_east()
        self.__move_south()
        self.__move_west()

    def __move_north(self):
        if self.__facing_north():
            self.__position = tuple(map(sum, zip(self.__position, (1, 0))))

    def __facing_north(self):
        return self.__direction == 2

    def __move_east(self):
        if self.__facing_east():
            self.__position = tuple(map(sum, zip(self.__position, (0, 1))))

    def __facing_east(self):
        return self.__direction == 1

    def __move_south(self):
        if self.__facing_south():
            self.__position = tuple(map(sum, zip(self.__position, (-1, 0))))

    def __facing_south(self):
        return self.__direction == 0

    def __move_west(self):
        if self.__facing_west():
            self.__position = tuple(map(sum, zip(self.__position, (0, -1))))

    def __facing_west(self):
        return self.__direction == 3

    def recharge(self, cost):
        self.__battery += cost

        if self.__battery > 100:
            self.__battery = 100

    def get_cycle(self):
        return self.__cycle

    def get_battery(self):
        return self.__battery

    def get_position(self):
        return self.__position

    def get_cleaned(self):
        return 0

    def get_render(self):
        if self.__facing_north():
            return "v"

        if self.__facing_east():
            return ">"

        if self.__facing_south():
            return "^"

        if self.__facing_west():
            return "<"

    def get_scan_position(self):
        if self.__facing_north():
            return self.__get_scan_north()

        if self.__facing_east():
            return self.__get_scan_east()

        if self.__facing_south():
            return self.__get_scan_south()

        if self.__facing_west():
            return self.__get_scan_west()

    def __get_scan_north(self):
        return tuple(map(sum, zip(self.__position, (1, 0))))

    def __get_scan_east(self):
        return tuple(map(sum, zip(self.__position, (0, 1))))

    def __get_scan_south(self):
        return tuple(map(sum, zip(self.__position, (-1, 0))))

    def __get_scan_west(self):
        return tuple(map(sum, zip(self.__position, (0, -1))))