#  Copyright (c) 2024. William E. Kitson

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class FuzzyFan:
    def __init__(self):
        self.__battery = ctrl.Antecedent(np.arange(0, 100, 1), 'battery')
        self.__initialise_battery()

        self.__dirt = ctrl.Antecedent(np.arange(0, 100, 1), 'dirt')
        self.__initialise_dirt()

        self.__fan_speed = ctrl.Consequent(np.arange(0, 100, 1), 'fan speed')
        self.__initialise_fan_speed()

        self.__fan_speed_control = self.__initialise_fan_speed_control()

    def __initialise_battery(self):
        self.__battery['low'] = fuzz.zmf(self.__battery.universe, 0, 25)
        self.__battery['medium'] = fuzz.trapmf(self.__battery.universe, [10, 40, 60, 80])
        self.__battery['high'] = fuzz.smf(self.__battery.universe, 75, 100)
        self.__battery.view()

    def __initialise_dirt(self):
        self.__dirt['thin'] = fuzz.zmf(self.__dirt.universe, 0, 50)
        self.__dirt['medium'] = fuzz.trapmf(self.__dirt.universe, [25, 40, 60, 75])
        self.__dirt['thick'] = fuzz.smf(self.__dirt.universe, 50, 100)
        self.__dirt.view()

    def __initialise_fan_speed(self):
        self.__fan_speed['slow'] = fuzz.zmf(self.__fan_speed.universe, 1, 50)
        self.__fan_speed['medium'] = fuzz.trapmf(self.__fan_speed.universe, [25, 50, 50, 75])
        self.__fan_speed['fast'] = fuzz.smf(self.__fan_speed.universe, 50, 100)
        self.__fan_speed.view()

    def __initialise_fan_speed_control(self):
        return ctrl.ControlSystem([
            ctrl.Rule(self.__battery['low'] & self.__dirt["thin"], self.__fan_speed['slow']),
            ctrl.Rule(self.__battery['high'] & self.__dirt["thick"], self.__fan_speed['fast']),
        ])

    def fan_speed(self, battery, dirt):
        fan_speed_sim = ctrl.ControlSystemSimulation(self.__fan_speed_control)
        fan_speed_sim.input['battery'] = battery
        fan_speed_sim.input['dirt'] = dirt
        fan_speed_sim.compute()
        self.__fan_speed.view(sim=fan_speed_sim)

        return fan_speed_sim.output['fan speed']