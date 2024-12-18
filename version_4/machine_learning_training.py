#  Copyright (c) 2024. William E. Kitson

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
import pandas as pd
# USE PICKLE TO SAVE TRAINED MODEL

class MachineLearningTraining:
    def __init__(self, dataset, answer_column):
        self.__data = pd.read_csv(dataset)
        self.__answer_column = answer_column
        self.__evaluated_models = []

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

        nearest_neighbour_evaluation = (
            accuracy_score(y_test, nearest_neighbour_prediction),
            recall_score(y_test, nearest_neighbour_prediction, average='macro'),
            precision_score(y_test, nearest_neighbour_prediction, average='macro'),
            f1_score(y_test, nearest_neighbour_prediction, average='macro'),
            matthews_corrcoef(y_test, nearest_neighbour_prediction)
        )

        nearest_neighbour_total = 0

        for i in nearest_neighbour_evaluation:
            nearest_neighbour_total += i

        self.__evaluated_models.append((
            nearest_neighbour_model,
            nearest_neighbour_evaluation,
            nearest_neighbour_total
        ))

    def render_evaluation(self):
        print(self.__evaluated_models)