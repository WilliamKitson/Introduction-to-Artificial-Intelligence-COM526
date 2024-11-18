class Pathfinder:
    def __init__(self):
        self.__nodes = []
        self.__position = (0, 0)

    def add_free(self, position):
        self.__nodes.append((position[0], position[1], 0, " "))

    def add_blocked(self, position):
        self.__nodes.append((position[0], position[1], 0, "x"))

    def get_node(self, position):
        for i in self.__nodes:
            if i[0] == position[0]:
                if i[1] == position[1]:
                    if i[2] == 0:
                        return "?"

                    return i[3]

    def get_scan_zone_north(self):
        return tuple(map(sum, zip(self.__position, (-1, 0))))

    def get_scan_zone_east(self):
        return tuple(map(sum, zip(self.__position, (0, 1))))

    def get_scan_zone_south(self):
        return tuple(map(sum, zip(self.__position, (1, 0))))

    def get_scan_zone_west(self):
        return tuple(map(sum, zip(self.__position, (0, -1))))

    def explore(self, position):
        self.__position = position

        for i, node in enumerate(self.__nodes):
            if node[0] == position[0]:
                if node[1] == position[1]:
                    self.__nodes[i] = (node[0], node[1], 1, node[3])