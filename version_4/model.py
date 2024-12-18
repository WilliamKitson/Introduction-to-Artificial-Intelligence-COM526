#  Copyright (c) 2024. William E. Kitson

import pickle

class Model:
    def __init__(self, filepath):
        with open(filepath, "rb") as f:
            self.__model = pickle.load(f)

    def predict(self, node_scan):
        return self.__model.predict(node_scan)