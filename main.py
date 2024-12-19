#  Copyright (c) 2024. William E. Kitson

from version_1.demonstration_version_1 import DemonstrationVersion1
from version_2.demonstration_version_2 import DemonstrationVersion2
from version_3.demonstration_version_3 import DemonstrationVersion3

with open("assets/COM526_map.txt", 'r') as file:
    file_content = file.read()

#DemonstrationVersion1(file_content).execute()
#DemonstrationVersion2(file_content).execute()
DemonstrationVersion3(file_content).execute()

from version_4.machine_learning_training import MachineLearningTraining
from version_4.model import Model

#training = MachineLearningTraining("assets/dataset.csv", "target")
#training.train()
#training.save_best_model("assets/model.pkl")
#print(training.render_evaluation())

scan_data = [[
    0.17075740533434242,
    -2.3105003225690215,
    1.0080232257946202,
    -0.6514677667048898,
    -0.07564270121366325,
    2.2591519295020803
]]

print(Model("assets/model.pkl").predict(scan_data))