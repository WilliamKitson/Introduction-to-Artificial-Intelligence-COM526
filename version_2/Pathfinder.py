class Pathfinder:
    def __init__(self, start):
        self.__nodes = []
        self.__start = start

    def add_node(self, node):
        self.__nodes.append(node)

    def render(self, position):
        if position == self.__start:
            return " "

        return "?"

    def get_node(self, position):
        for i in self.__nodes:
            if i[0] == position[0]:
                if i[1] == position[1]:
                    return i[2]