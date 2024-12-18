#  Copyright (c) 2024. William E. Kitson

from version_1.demonstration_version_1 import DemonstrationVersion1
from version_2.demonstration_version_2 import DemonstrationVersion2
from version_3.demonstration_version_3 import DemonstrationVersion3
from version_4.machine_learning_training import MachineLearningTraining

with open("COM526_map.txt", 'r') as file:
    file_content = file.read()

#DemonstrationVersion1(file_content).execute()
#DemonstrationVersion2(file_content).execute()
#DemonstrationVersion3(file_content).execute()

training = MachineLearningTraining("version_4/dataset.csv", "target")
training.train()
model = training.get_best_model()

print(training.render_evaluation())
print(model)