#  Copyright (c) 2024. William E. Kitson

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class FuzzyCleaning:
    def __init__(self):
        self.__cleaning_rate = ctrl.Consequent(np.arange(0, 20, 1), "cleaning rate")
        self.__initialise_cleaning_rate()

        self.__fan_speed = ctrl.Antecedent(np.arange(0, 100, 1), "fan speed")
        self.__initialise_fan_speed()

        self.__cleaning_rate_control = self.__initialise_cleaning_rate_control()
        self.__cleaning_rate_sim = ctrl.ControlSystemSimulation(self.__cleaning_rate_control)

    def __initialise_cleaning_rate(self):
        self.__cleaning_rate["low"] = fuzz.zmf(self.__cleaning_rate.universe, 0, 8)
        self.__cleaning_rate["medium"] = fuzz.trapmf(self.__cleaning_rate.universe, [4, 8, 12, 16])
        self.__cleaning_rate["high"] = fuzz.smf(self.__cleaning_rate.universe, 12, 20)

    def __initialise_fan_speed(self):
        self.__fan_speed["slow"] = fuzz.zmf(self.__fan_speed.universe, 0, 50)
        self.__fan_speed["medium"] = fuzz.trapmf(self.__fan_speed.universe, [25, 50, 50, 75])
        self.__fan_speed["fast"] = fuzz.smf(self.__fan_speed.universe, 50, 100)

    def __initialise_cleaning_rate_control(self):
        drain_slow = ctrl.Rule(
            self.__fan_speed["slow"],
            self.__cleaning_rate["low"]
        )

        drain_medium = ctrl.Rule(
            self.__fan_speed["medium"],
            self.__cleaning_rate["medium"]
        )

        drain_fast = ctrl.Rule(
            self.__fan_speed["fast"],
            self.__cleaning_rate["high"]
        )

        return ctrl.ControlSystem([
            drain_slow,
            drain_medium,
            drain_fast
        ])

    def calculate(self, fan_speed):
        self.__cleaning_rate_sim.input["fan speed"] = fan_speed
        self.__cleaning_rate_sim.compute()

    def get_cleaning_rate(self):
        return self.__cleaning_rate_sim.output["cleaning rate"]

    def render(self):
        self.__cleaning_rate.view()
        self.__fan_speed.view()
        self.__cleaning_rate.view(sim=self.__cleaning_rate_sim)

    def test(self):
        for i in range(0, 101):
            self.calculate(i)

            print(
                f"cleaning rate: {self.get_cleaning_rate()}\n"
                f"fan speed input: {i}\n"
            )