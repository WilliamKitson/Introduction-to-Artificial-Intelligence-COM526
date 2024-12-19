#  Copyright (c) 2024. William E. Kitson

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class FuzzyBattery:
    def __init__(self):
        self.__fan_speed = ctrl.Antecedent(np.arange(0, 100, 1), "fan speed")
        self.__initialise_fan_speed()

        self.__battery_drain = ctrl.Consequent(np.arange(0, 10, 1), "battery drain")
        self.__initialise_battery_drain()

        self.__battery_drain_control = self.__initialise_battery_drain_control()
        self.__battery_drain_sim = ctrl.ControlSystemSimulation(self.__battery_drain_control)

    def __initialise_fan_speed(self):
        self.__fan_speed["slow"] = fuzz.zmf(self.__fan_speed.universe, 0, 50)
        self.__fan_speed["medium"] = fuzz.trapmf(self.__fan_speed.universe, [25, 50, 50, 75])
        self.__fan_speed["fast"] = fuzz.smf(self.__fan_speed.universe, 50, 100)

    def __initialise_battery_drain(self):
        self.__battery_drain["slow"] = fuzz.zmf(self.__battery_drain.universe, 0, 4)
        self.__battery_drain["medium"] = fuzz.trapmf(self.__battery_drain.universe, [2, 4, 6, 8])
        self.__battery_drain["fast"] = fuzz.smf(self.__battery_drain.universe, 6, 10)

    def __initialise_battery_drain_control(self):
        drain_slow = ctrl.Rule(
            self.__fan_speed["slow"],
            self.__battery_drain["slow"]
        )

        drain_medium = ctrl.Rule(
            self.__fan_speed["medium"],
            self.__battery_drain["medium"]
        )

        drain_fast = ctrl.Rule(
            self.__fan_speed["fast"],
            self.__battery_drain["fast"]
        )

        return ctrl.ControlSystem([
            drain_slow,
            drain_medium,
            drain_fast
        ])

    def calculate(self, fan_speed):
        self.__battery_drain_sim.input["fan speed"] = fan_speed
        self.__battery_drain_sim.compute()

    def get_battery_drain(self):
        return self.__battery_drain_sim.output["battery drain"]

    def render(self):
        self.__battery_drain.view()
        self.__fan_speed.view()
        self.__battery_drain.view(sim=self.__battery_drain_sim)

    def test(self):
        for i in range(0, 101):
            self.calculate(i)

            print(
                f"battery drain: {self.get_battery_drain()}\n"
                f"fan speed input: {i}\n"
            )