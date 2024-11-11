from map import Map
from cleaner import Cleaner
from charger import Charger

class Version1:
    def __init__(self, map_data):
        self.__map = Map(map_data)
        self.__cleaner = Cleaner(self.__map.get_start())
        self.__charger = Charger(self.__map.get_charger())

    def execute(self):
        while self.__cleaner.get_battery():
            self.__render()
            self.__sense()
            self.__cycle()

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

        if self.__charger.get_charge_zone() == (x, y):
            return "c"

        return self.__map.get_render((x, y))

    def __render_stats(self):
        return (
            f"cycle: {self.__cleaner.get_cycle()}\n"
            f"battery: {self.__cleaner.get_battery()}\n"
            f"dirt: {self.__map.get_dirt(self.__cleaner.get_position())}\n"
        )

    def __sense(self):
        self.__cleaner.sense(
            self.__map.get_dirt(self.__cleaner.get_position()),
            self.__map.get_blocked(self.__cleaner.get_scan_position())
        )

    def __cycle(self):
        self.__cleaner.cycle()
        self.__cleaner.recharge(self.__charger.get_charge(self.__cleaner.get_position()))