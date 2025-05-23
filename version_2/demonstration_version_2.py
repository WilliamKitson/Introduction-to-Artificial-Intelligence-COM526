#  Copyright (c) 2024. William E. Kitson

from version_2.map import Map
from version_2.cleaner import Cleaner
from version_2.charger import Charger
from version_2.local_knowledge import LocalKnowledge
from version_2.pathfinder import Pathfinder

class DemonstrationVersion2:
    def __init__(self, map_data):
        self.__map = Map(map_data)
        self.__cleaner = Cleaner(self.__map.get_start())
        self.__charger = Charger(self.__map.get_charger())
        self.__local_knowledge = LocalKnowledge()
        self.__load_local_knowledge()
        self.__pathfinder = Pathfinder()

    def __load_local_knowledge(self):
        for x in range(0, self.__map.get_width()):
            self.__load_local_knowledge_y(x)

    def __load_local_knowledge_y(self, x):
        for y in range(0, self.__map.get_height()):
            self.__load_local_knowledge_node((x, y))

    def __load_local_knowledge_node(self, position):
        if self.__map.get_render(position) in "^":
            self.__local_knowledge.add_free(position, "0")

        if self.__map.get_render(position) in " ":
            self.__local_knowledge.add_free(position, self.__map.get_dirt(position))

        if self.__map.get_render(position) in "x":
            self.__local_knowledge.add_blocked(position)

        if self.__map.get_charger() == position:
            self.__local_knowledge.add_charger(position)

    def execute(self):
        while self.__execute_condition():
            self.__sense()
            self.__cycle()
            self.__render()
            input("press enter to continue\n")

    def __execute_condition(self):
        if self.__cleaner.get_battery() <= 0:
            return False

        if self.__cleaner.get_cycle() > 250:
            return False

        return True

    def __sense(self):
        self.__cleaner.sense(
            self.__map.get_dirt(self.__cleaner.get_position()),
            self.__map.get_blocked(self.__cleaner.get_scan_position())
        )

    def __cycle(self):
        if self.__cleaner.get_battery() < 33:
            self.__hunt_charger()

        self.__hunt_dirt()
        self.__cleaner.cycle()
        self.__local_knowledge.explore(self.__cleaner.get_position())
        self.__apply_cleaning()
        self.__cleaner.recharge(self.__charger.get_charge(self.__cleaner.get_position()))

    def __hunt_charger(self):
        if self.__hunt_charger_impossible():
            return

        self.__pathfinder.calculate(
            self.__generate_pathfinder_map(),
            self.__cleaner.get_position(),
            self.__charger.get_charge_zone()
        )

        self.__cleaner.set_path(self.__pathfinder.get_path())

    def __hunt_charger_impossible(self):
        if not self.__local_knowledge.charger_located():
            return False

        if self.__cleaner.has_path():
            return False

        return True

    def __generate_pathfinder_map(self):
        pathfinder_map = []

        for i in range(0, self.__map.get_width()):
            map_row = []

            for j in range(0, self.__map.get_height()):
                map_row.append(int(self.__local_knowledge.get_node((i, j)) not in ("x", "u", "?")))

            pathfinder_map.append(map_row)

        return pathfinder_map

    def __apply_cleaning(self):
        position = self.__cleaner.get_position()

        self.__map.set_dirt(
            position,
            self.__calculate_cleaned_dirt()
        )

        self.__local_knowledge.update_free(
            self.__cleaner.get_position(),
            self.__map.get_dirt(position)
        )

    def __calculate_cleaned_dirt(self):
        return int(self.__map.get_dirt(self.__cleaner.get_position())) - self.__cleaner.get_cleaned()

    def __hunt_dirt(self):
        if self.__pathfinder.get_path():
            return

        if self.__map.get_dirt(self.__cleaner.get_position()):
            return

        self.__pathfinder.calculate(
            self.__generate_pathfinder_map(),
            self.__cleaner.get_position(),
            self.__local_knowledge.get_priority()
        )

        self.__cleaner.set_path(self.__pathfinder.get_path())

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
            f"\ndirt: {self.__map.get_dirt(self.__cleaner.get_position())}"
            f"\nlast path: {self.__pathfinder.get_path()}\n"
        )