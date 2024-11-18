class Pathfinder:
    def __init__(self):
        self.__nodes = []
        self.__position = (0, 0)

    def add_free(self, position):
        self.__nodes.append((position[0], position[1], 0, " "))

    def add_blocked(self, position):
        self.__nodes.append((position[0], position[1], 0, "x"))

    def get_node(self, position):
        node_at = self.__get_node_at(position)

        if node_at[2] == 0:
            return "?"

        return node_at[3]

    def __get_node_at(self, position):
        for node in self.__nodes:
            if (node[0], node[1]) == position:
                return node

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