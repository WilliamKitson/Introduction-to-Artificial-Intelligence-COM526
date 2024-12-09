#  Copyright (c) 2024. William E. Kitson

from version_1.demonstration_version_1 import DemonstrationVersion1
from version_2.demonstration_version_2 import DemonstrationVersion2

with open("maps/COM526_map_simple.txt", 'r') as file:
    file_content = file.read()

#DemonstrationVersion1(file_content).execute()
#DemonstrationVersion2(file_content).execute()

from version_3.fuzzy_fan import FuzzyFan

fuzzy_fan = FuzzyFan()

print(fuzzy_fan.fan_speed(100, 100))
fuzzy_fan.render()