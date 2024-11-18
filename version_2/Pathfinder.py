class Pathfinder:
    def __init__(self):
        self.__nodes = []
        self.__position = (0, 0)

    def add_free(self, position):
        self.__nodes.append((position[0], position[1], 0, " "))

    def add_blocked(self, position):
        self.__nodes.append((position[0], position[1], 0, "x"))

    def get_node(self, position):
        return self.__get_node_value(self.__get_node_at(position))

    def __get_node_value(self, node):
        if node[2] == 0:
            return "?"

        return node[3]

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
        self.__explore_node(position)

    def __explore_node(self, position):
        for i, node in enumerate(self.__nodes):
            if (node[0], node[1]) == position:
                self.__nodes[i] = (node[0], node[1], 1, node[3])