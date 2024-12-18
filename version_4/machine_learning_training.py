#  Copyright (c) 2024. William E. Kitson

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
import pandas as pd

class MachineLearningTraining:
    def __init__(self, dataset, answer_column):
        self.__data = pd.read_csv(dataset)
        self.__answer_column = answer_column
        self.__evaluation = []

    def train(self):
        questions = self.__data.drop([self.__answer_column], axis=1)
        answers = self.__data[self.__answer_column]

        x_train, x_test, y_train, y_test = train_test_split(
            questions,
            answers,
            test_size=0.2
        )

        nearest_neighbour = KNeighborsClassifier(n_neighbors=3)
        nearest_neighbour_model = nearest_neighbour.fit(questions, answers)
        nearest_neighbour_prediction = nearest_neighbour_model.predict(x_test)

        print(f"Accuracy is {accuracy_score(y_test, nearest_neighbour_prediction)}")
        print(f"Recall is {recall_score(y_test, nearest_neighbour_prediction, average='macro')}")
        print(f"Precision is {precision_score(y_test, nearest_neighbour_prediction, average='macro')}")
        print(f"F1-Score is {f1_score(y_test, nearest_neighbour_prediction, average='macro')}")
        print(f"MCC is {matthews_corrcoef(y_test, nearest_neighbour_prediction)}")