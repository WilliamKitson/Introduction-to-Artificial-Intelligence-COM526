#  Copyright (c) 2024. William E. Kitson

from version_2.map import Map
from version_2.cleaner import Cleaner
from version_2.charger import Charger
from version_2.local_knowledge import LocalKnowledge

class DemonstrationVersion2:
    def __init__(self, map_data):
        self.__map = Map(map_data)
        self.__cleaner = Cleaner(self.__map.get_start())
        self.__charger = Charger(self.__map.get_charger())
        self.__local_knowledge = LocalKnowledge()
        self.__load_local_knowledge()

    def __load_local_knowledge(self):
        for x in range(0, self.__map.get_width()):
            for y in range(0, self.__map.get_height()):
                if self.__map.get_render((x, y)) == " ":
                    self.__local_knowledge.add_free((x, y))

                if self.__map.get_render((x, y)) == "x":
                    self.__local_knowledge.add_blocked((x, y))

    def execute(self):
        while self.__cleaner.get_battery():
            self.__sense()
            self.__cycle()
            self.__render()

    def __sense(self):
        self.__cleaner.sense(
            self.__map.get_dirt(self.__cleaner.get_position()),
            self.__map.get_blocked(self.__cleaner.get_scan_position())
        )

    def __cycle(self):
        self.__cleaner.cycle()
        self.__local_knowledge.explore(self.__cleaner.get_position())

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

        return self.__local_knowledge.get_node((x, y))

    def __render_stats(self):
        return (
            f"\ncycle: {self.__cleaner.get_cycle()}"
            f"\nposition: {self.__cleaner.get_position()}"
            f"\nbattery: {self.__cleaner.get_battery()}"
            f"\ndirt: {self.__map.get_dirt(self.__cleaner.get_position())}\n"
        )