#  Copyright (c) 2024. William E. Kitson

from version_1.demonstration_version_1 import DemonstrationVersion1
from version_2.demonstration_version_2 import DemonstrationVersion2

with open("maps/COM526_map_simple.txt", 'r') as file:
    file_content = file.read()

DemonstrationVersion1(file_content).execute()
DemonstrationVersion2(file_content).execute()

from version_3.fuzzy_fan import FuzzyFan
from version_3.fuzzy_battery import FuzzyBattery
from version_3.fuzzy_cleaning import FuzzyCleaning

fuzzy_fan = FuzzyFan()
fuzzy_fan.calculate(100, 100)
print(fuzzy_fan.get_fan_speed())

fuzzy_battery = FuzzyBattery()
fuzzy_battery.calculate(fuzzy_fan.get_fan_speed())
print(fuzzy_battery.get_battery_drain())

fuzzy_cleaning = FuzzyCleaning()
fuzzy_cleaning.calculate(fuzzy_fan.get_fan_speed())
print(fuzzy_cleaning.get_cleaning_rate())