#  Copyright (c) 2024. William E. Kitson

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
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

        self.__train_classifier(KNeighborsClassifier(n_neighbors=3), questions, answers, x_test, y_test)
        self.__train_classifier(DecisionTreeClassifier(), questions, answers, x_test, y_test)

    def __train_classifier(self, classifier, questions, answers, x_test, y_test):
        model = classifier.fit(questions, answers)
        prediction = model.predict(x_test)

        evaluation = (
            accuracy_score(y_test, prediction),
            recall_score(y_test, prediction, average='macro'),
            precision_score(y_test, prediction, average='macro'),
            f1_score(y_test, prediction, average='macro'),
            matthews_corrcoef(y_test, prediction)
        )

        total = 0

        for i in evaluation:
            total += i

        total /= len(evaluation)

        self.__evaluated_models.append((
            model,
            evaluation,
            total
        ))

    def render_evaluation(self):
        output = ""

        for i in self.__evaluated_models:
            output += (
                f"model: {i[0]}\n"
                f"accuracy: {i[1][0]}\n"
                f"recall: {i[1][1]}\n"
                f"precision: {i[1][2]}\n"
                f"f1: {i[1][3]}\n"
                f"matthews: {i[1][4]}\n"
                f"total: {i[2]}\n\n"
            )

        return output