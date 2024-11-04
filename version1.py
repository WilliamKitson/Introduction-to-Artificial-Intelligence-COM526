from map import Map
from cleaner import Cleaner

class Version1:
    def __init__(self, map_data):
        self.__map = Map(map_data)
        self.__cleaner = Cleaner(1, 1)

    def execute(self):
        while self.__cleaner.get_battery():
            self.__render()
            self.__sense()
            self.__cleaner.cycle()

    def __sense(self):
        self.__cleaner.set_scan(self.__map.get_blocked(
            self.__cleaner.get_scan()[0],
            self.__cleaner.get_scan()[1]
        ))

    def __render(self):
        render = ""

        for i in range(0, self.__map.get_height()):
            render += self.__render_y(i)
            render += "\n"

        print(render)

    def __render_y(self, x):
        row = ""

        for i in range(0, self.__map.get_width()):
            row += self.__render_node(x, i)

        return row

    def __render_node(self, x, y):
        if self.__cleaner.get_position() == (x, y):
            return self.__cleaner.get_render()

        return self.__map.get_render(x, y)