#  Copyright (c) 2024. William E. Kitson

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class FuzzyFan:
    def __init__(self):
        self.__battery = ctrl.Antecedent(np.arange(0, 100, 1), "battery")
        self.__initialise_battery()

        self.__dirt = ctrl.Antecedent(np.arange(0, 9, 1), "dirt")
        self.__initialise_dirt()

        self.__fan_speed = ctrl.Consequent(np.arange(0, 100, 1), "fan speed")
        self.__initialise_fan_speed()

        self.__fan_speed_control = self.__initialise_fan_speed_control()
        self.__fan_speed_sim = ctrl.ControlSystemSimulation(self.__fan_speed_control)

    def __initialise_battery(self):
        self.__battery["low"] = fuzz.zmf(self.__battery.universe, 0, 50)
        self.__battery["medium"] = fuzz.trapmf(self.__battery.universe, [25, 50, 50, 75])
        self.__battery["high"] = fuzz.smf(self.__battery.universe, 50, 100)

    def __initialise_dirt(self):
        self.__dirt["thin"] = fuzz.zmf(self.__dirt.universe, 0, 5)
        self.__dirt["medium"] = fuzz.trapmf(self.__dirt.universe, [2, 4, 6, 8])
        self.__dirt["thick"] = fuzz.smf(self.__dirt.universe, 5, 9)

    def __initialise_fan_speed(self):
        self.__fan_speed["slow"] = fuzz.zmf(self.__fan_speed.universe, 0, 50)
        self.__fan_speed["medium"] = fuzz.trapmf(self.__fan_speed.universe, [25, 50, 50, 75])
        self.__fan_speed["fast"] = fuzz.smf(self.__fan_speed.universe, 50, 100)

    def __initialise_fan_speed_control(self):
        low_battery_speed = ctrl.Rule(
            self.__battery["low"] or self.__dirt["thin"],
            self.__fan_speed["slow"]
        )

        medium_battery_speed = ctrl.Rule(
            self.__battery["medium"] or self.__dirt["medium"],
            self.__fan_speed["slow"]
        )

        high_speed = ctrl.Rule(
            self.__battery["high"] and self.__dirt["thick"],
            self.__fan_speed["fast"]
        )

        high_dirt_speed = ctrl.Rule(
            self.__dirt["thick"],
            self.__fan_speed["fast"]
        )

        return ctrl.ControlSystem([
            low_battery_speed,
            medium_battery_speed,
            high_speed,
            high_dirt_speed
        ])

    def calculate(self, battery, dirt):
        self.__fan_speed_sim.input["battery"] = battery
        self.__fan_speed_sim.input["dirt"] = dirt
        self.__fan_speed_sim.compute()

    def get_fan_speed(self):
        return self.__fan_speed_sim.output["fan speed"]

    def render(self):
        self.__battery.view()
        self.__dirt.view()
        self.__fan_speed.view()
        self.__fan_speed.view(sim=self.__fan_speed_sim)

    def test(self):
        for i in range(0, 100):
            for j in range(0, 9):
                fuzzy_fan = FuzzyFan()
                fuzzy_fan.calculate(i, j)

                print(
                    f"fan speed: {fuzzy_fan.get_fan_speed()}\n"
                    f"battery input: {i}, dirt input: {j}\n"
                )