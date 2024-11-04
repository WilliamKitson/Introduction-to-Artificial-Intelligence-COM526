from map import Map
from cleaner import Cleaner
import time

class Version1:
    def __init__(self, map_data):
        self.__map = Map(map_data)
        self.__cleaner = Cleaner(1, 1)

    def execute(self):
        print(f"map width: {self.__map.get_width()}, height: {self.__map.get_height()}")

        while self.__cleaner.get_battery():
            self.__cleaner.set_scan(self.__map.get_blocked(self.__cleaner.get_scan()[0], self.__cleaner.get_scan()[1]))
            self.__cleaner.cycle()

            print(f"cycle {self.__cleaner.get_cycle()}: {self.__cleaner.get_render()} ({self.__cleaner.get_battery()}%)")
            time.sleep(1)