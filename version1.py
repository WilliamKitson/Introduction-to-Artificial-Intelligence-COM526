from charger import Charger
from map import Map
from cleaner import Cleaner

class Version1:
    def __init__(self, filepath):
        self.__map = Map(self.__load_map(filepath))

        self.__cleaner = Cleaner(
            self.__map.get_start()[0],
            self.__map.get_start()[1]
        )

        self.__charger = Charger(
            1,
            1
        )

    @staticmethod
    def __load_map(filepath):
        with open(filepath, 'r') as file:
            file_content = file.read()

        return file_content

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
        print(self.__render_x(), self.__render_stats())

    def __render_x(self):
        render = ""

        for i in range(0, self.__map.get_height()):
            render += self.__render_y(i)
            render += "\n"

        return render

    def __render_y(self, x):
        render = ""

        for i in range(0, self.__map.get_width()):
            render += self.__render_node(x, i)

        return render

    def __render_node(self, x, y):
        if self.__cleaner.get_position() == (x, y):
            return self.__cleaner.get_render()

        if self.__charger.get_position() == (x, y):
            return self.__charger.get_render()

        return self.__map.get_render(x, y)

    def __render_stats(self):
        return (
            f"cycle: {self.__cleaner.get_cycle()}\n"
            f" battery: {self.__cleaner.get_battery()}\n"
        )