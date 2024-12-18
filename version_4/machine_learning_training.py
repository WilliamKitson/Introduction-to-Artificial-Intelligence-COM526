#  Copyright (c) 2024. William E. Kitson

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

data = pd.read_csv("dataset.csv")

X = data.drop(["target"], axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

neigh = KNeighborsClassifier(n_neighbors=3)
knn_model = neigh.fit(X, y)
knn_pred = knn_model.predict(X_test)

print(f"KNN accuracy is {accuracy_score(y_test, knn_pred)}")