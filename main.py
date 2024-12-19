#  Copyright (c) 2024. William E. Kitson

from version_1.demonstration_version_1 import DemonstrationVersion1
from version_2.demonstration_version_2 import DemonstrationVersion2
from version_3.demonstration_version_3 import DemonstrationVersion3
from version_4.demonstration_version_4 import DemonstrationVersion4

with open("assets/COM526_map.txt", 'r') as file:
    map_data = file.read()

version_1 = DemonstrationVersion1(map_data)
#version_1.execute()

version_2 = DemonstrationVersion2(map_data)
#version_2.execute()

version_3 = DemonstrationVersion3(map_data)
#version_3.execute()
#version_3.test_fuzzy_logic()

version_4 = DemonstrationVersion4(
    map_data,
    "assets/readings.json",
    "assets/dataset.csv",
    "assets/model.pkl"
)

version_4.execute()
#version_4.retrain_model("assets/model.pkl")