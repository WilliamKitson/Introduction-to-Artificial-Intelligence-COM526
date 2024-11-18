class Pathfinder:
    def __init__(self):
        self.__nodes = []
        self.__position = (0, 0)

    def add_node(self, node):
        self.__nodes.append(node)

    def get_node(self, position):
        for i in self.__nodes:
            if i[0] == position[0]:
                if i[1] == position[1]:
                    return i[2]

        return "?"

    def get_scan_zone_north(self):
        return tuple(map(sum, zip(self.__position, (-1, 0))))

    def set_position(self, position):
        self.__position = position