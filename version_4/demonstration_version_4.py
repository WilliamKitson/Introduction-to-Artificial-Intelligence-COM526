#  Copyright (c) 2024. William E. Kitson

from version_4.map import Map
from version_4.cleaner import Cleaner
from version_4.charger import Charger
from version_4.local_knowledge import LocalKnowledge
from version_4.pathfinder import Pathfinder
from version_4.fuzzy_fan import FuzzyFan
from version_4.fuzzy_battery import FuzzyBattery
from version_4.fuzzy_cleaning import FuzzyCleaning
from version_4.machine_learning_training import MachineLearningTraining
from version_4.model import Model

class DemonstrationVersion4:
    def __init__(self, map_data, dataset_filepath, model_filepath):
        self.__map = Map(map_data)
        self.__cleaner = Cleaner(self.__map.get_start())
        self.__charger = Charger(self.__map.get_charger())
        self.__local_knowledge = LocalKnowledge()
        self.__load_local_knowledge()
        self.__pathfinder = Pathfinder()
        self.__fuzzy_fan = FuzzyFan()
        self.__fuzzy_battery = FuzzyBattery()
        self.__fuzzy_cleaning = FuzzyCleaning()
        self.__training = MachineLearningTraining(dataset_filepath, "target")
        self.__model = Model(model_filepath)

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
            self.__local_knowledge.add_free(position, int(self.__map.get_dirt(position)))

        if self.__map.get_render(position) in "x":
            self.__local_knowledge.add_blocked(position)

        if self.__map.get_charger() == position:
            self.__local_knowledge.add_charger(position)

    def execute(self):
        scan_data = [[
            0.17075740533434242,
            -2.3105003225690215,
            1.0080232257946202,
            -0.6514677667048898,
            -0.07564270121366325,
            2.2591519295020803
        ]]

        print(self.__model.predict(scan_data))

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

        self.__fuzzy_fan.calculate(
            self.__cleaner.get_battery(),
            self.__map.get_dirt(position)
        )

        self.__fuzzy_battery.calculate(
            self.__fuzzy_fan.get_fan_speed()
        )

        self.__cleaner.decrement_battery(
            self.__fuzzy_battery.get_battery_drain()
        )

        self.__fuzzy_cleaning.calculate(
            self.__fuzzy_fan.get_fan_speed()
        )

        self.__map.set_dirt(
            position,
            self.__calculate_cleaned()
        )

        self.__local_knowledge.update_free(
            self.__cleaner.get_position(),
            self.__map.get_dirt(position)
        )

    def __calculate_cleaned(self):
        dirt = self.__map.get_dirt(self.__cleaner.get_position())
        dirt -= float(self.__fuzzy_cleaning.get_cleaning_rate())

        if dirt < 0:
            dirt = 0

        return dirt

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

        if self.__local_knowledge.get_node((x,y)) in ("?", "x"):
            return self.__local_knowledge.get_node((x,y))

        return str(int(float(self.__local_knowledge.get_node((x, y)))))

    def __render_stats(self):
        return (
            f"\ncycle: {self.__cleaner.get_cycle()}"
            f"\nposition: {self.__cleaner.get_position()}"
            f"\nbattery: {self.__cleaner.get_battery()}"
            f"\ndirt: {self.__map.get_dirt(self.__cleaner.get_position())}"
            f"\nlast path: {self.__pathfinder.get_path()}"
            f"\nfan speed: {self.__fuzzy_fan.get_fan_speed()}"
            f"\nbattery drain: {self.__fuzzy_battery.get_battery_drain()}"
            f"\ncleaning rate: {self.__fuzzy_cleaning.get_cleaning_rate()}\n"
        )

    def test_fuzzy_logic(self):
        self.__fuzzy_fan.test()
        self.__fuzzy_battery.test()
        self.__fuzzy_cleaning.test()

    def retrain_model(self, model_filepath):
        self.__training.train()
        self.__training.save_best_model(model_filepath)
        print(self.__training.render_evaluation())