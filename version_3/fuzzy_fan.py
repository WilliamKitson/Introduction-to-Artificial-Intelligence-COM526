#  Copyright (c) 2024. William E. Kitson

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class FuzzyFan:
    def __init__(self):
        self.__battery = ctrl.Antecedent(np.arange(0, 100, 1), "battery")
        self.__initialise_battery()

        self.__dirt = ctrl.Antecedent(np.arange(0, 100, 1), "dirt")
        self.__initialise_dirt()

        self.__fan_speed = ctrl.Consequent(np.arange(0, 100, 1), "fan speed")
        self.__initialise_fan_speed()

        self.__fan_speed_control = self.__initialise_fan_speed_control()
        self.__fan_speed_sim = ctrl.ControlSystemSimulation(self.__fan_speed_control)

    def __initialise_battery(self):
        self.__battery["low"] = fuzz.zmf(self.__battery.universe, 0, 25)
        self.__battery["medium"] = fuzz.trapmf(self.__battery.universe, [10, 40, 60, 80])
        self.__battery["high"] = fuzz.smf(self.__battery.universe, 75, 100)

    def __initialise_dirt(self):
        self.__dirt["thin"] = fuzz.zmf(self.__dirt.universe, 0, 50)
        self.__dirt["medium"] = fuzz.trapmf(self.__dirt.universe, [25, 40, 60, 75])
        self.__dirt["thick"] = fuzz.smf(self.__dirt.universe, 50, 100)

    def __initialise_fan_speed(self):
        self.__fan_speed["slow"] = fuzz.zmf(self.__fan_speed.universe, 0, 50)
        self.__fan_speed["medium"] = fuzz.trapmf(self.__fan_speed.universe, [25, 50, 50, 75])
        self.__fan_speed["fast"] = fuzz.smf(self.__fan_speed.universe, 50, 100)

    def __initialise_fan_speed_control(self):
        low_speed = ctrl.Rule(
            self.__battery["low"] or self.__dirt["thin"],
            self.__fan_speed["slow"]
        )

        medium_speed = ctrl.Rule(
            self.__battery["medium"] or self.__dirt["medium"],
            self.__fan_speed["slow"]
        )

        high_speed = ctrl.Rule(
            self.__battery["high"] & self.__dirt["thick"],
            self.__fan_speed["fast"]
        )

        return ctrl.ControlSystem([
            low_speed,
            medium_speed,
            high_speed
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