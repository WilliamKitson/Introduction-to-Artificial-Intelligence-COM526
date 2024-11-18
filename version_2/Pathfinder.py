class Pathfinder:
    def __init__(self, start):
        self.__start = start

    def render(self, position):
        if position == self.__start:
            return " "

        return "?"