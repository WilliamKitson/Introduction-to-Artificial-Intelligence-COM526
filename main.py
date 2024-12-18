#  Copyright (c) 2024. William E. Kitson

from version_1.demonstration_version_1 import DemonstrationVersion1
from version_2.demonstration_version_2 import DemonstrationVersion2
from version_3.demonstration_version_3 import DemonstrationVersion3

with open("COM526_map.txt", 'r') as file:
    file_content = file.read()

#DemonstrationVersion1(file_content).execute()
#DemonstrationVersion2(file_content).execute()
#DemonstrationVersion3(file_content).execute()

from version_4.machine_learning_training import MachineLearningTraining
import pickle

def train_model():
    training = MachineLearningTraining("version_4/dataset.csv", "target")
    training.train()
    print(training.render_evaluation())

    with open('model.pkl','wb') as f:
        pickle.dump(training.get_best_model(), f)

#train_model()

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

scan_data = [[
    -1.2332742655295212,
    2.758632998977856,
    0.47467562379722095,
    5.915661330860918,
    0.2574279551555407,
    -4.3400370105057515
]]

print(model.predict(scan_data))