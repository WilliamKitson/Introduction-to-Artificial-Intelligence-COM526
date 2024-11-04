from map import Map
from cleaner import Cleaner
import time

class Version1:
    def __init__(self, map_data):
        self.__map = Map(map_data)
        self.__cleaner = Cleaner(1, 1)

    def execute(self):
        while self.__cleaner.get_battery():
            self.__sense()
            self.__cleaner.cycle()
            self.__render()
            time.sleep(1)

    def __sense(self):
        self.__cleaner.set_scan(self.__map.get_blocked(
            self.__cleaner.get_scan()[0],
            self.__cleaner.get_scan()[1]
        ))

    def __render(self):
        render = ""

        for i in range(0, self.__map.get_height()):
            for j in range(0, self.__map.get_width()):
                if self.__cleaner.get_position() == (i, j):
                    render += self.__cleaner.get_render()

                else:
                    render += self.__map.get_render(i, j)

            render += "\n"

        print(render)