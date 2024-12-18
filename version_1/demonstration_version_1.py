#  Copyright (c) 2024. William E. Kitson

from version_1.map import Map
from version_1.cleaner import Cleaner
from version_1.charger import Charger

class DemonstrationVersion1:
    def __init__(self, map_data):
        self.__map = Map(map_data)
        self.__cleaner = Cleaner(self.__map.get_start())
        self.__charger = Charger(self.__map.get_charger())

    def execute(self):
        while self.__cleaner.get_battery():
            self.__sense()
            self.__cycle()
            self.__render()
            input("press enter to continue\n")

    def __sense(self):
        self.__cleaner.sense(
            self.__map.get_dirt(self.__cleaner.get_position()),
            self.__map.get_blocked(self.__cleaner.get_scan_position())
        )

    def __cycle(self):
        self.__cleaner.cycle()

        self.__map.set_dirt(
            self.__cleaner.get_position(),
            self.__calculate_cleaned_dirt()
        )

        self.__cleaner.recharge(self.__charger.get_charge(self.__cleaner.get_position()))

    def __calculate_cleaned_dirt(self):
        return int(self.__map.get_dirt(self.__cleaner.get_position())) - self.__cleaner.get_cleaned()

    def __render(self):
        print(self.__render_x(), self.__render_stats())

    def __render_x(self):
        render = ""

        for i in range(0, self.__map.get_width()):
            render += self.__render_y(i)
            render += "\n"

        return render

    def __render_y(self, x):
        render = ""

        for i in range(0, self.__map.get_height()):
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
            f"\ncycle: {self.__cleaner.get_cycle()}"
            f"\nposition: {self.__cleaner.get_position()}"
            f"\nbattery: {self.__cleaner.get_battery()}"
            f"\ndirt: {self.__map.get_dirt(self.__cleaner.get_position())}"
        )