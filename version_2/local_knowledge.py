#  Copyright (c) 2024. William E. Kitson

class LocalKnowledge:
    def __init__(self):
        self.__nodes = []
        self.__position = (0, 0)

    def add_free(self, position, dirt):
        self.__nodes.append((position[0], position[1], 0, str(dirt)))

    def add_blocked(self, position):
        self.__nodes.append((position[0], position[1], 0, "x"))

    def add_charger(self, position):
        self.__nodes.append((position[0], position[1], 0, "u"))

    def update_free(self, position, dirt):
        free_node_index = self.__get_node_index_at(position)
        free_node = self.__nodes[free_node_index]

        updated_node = (free_node[0], free_node[1], free_node[2], str(dirt))
        self.__nodes[free_node_index] = updated_node

    def get_node(self, position):
        try:
            return self.__get_node_value(self.__get_node_index_at(position))

        except IndexError:
            return "?"

    def __get_node_index_at(self, position):
        for i, node in enumerate(self.__nodes):
            if (node[0], node[1]) == position:
                return i

        raise IndexError

    def __get_node_value(self, index):
        node = self.__nodes[index]

        if node[2] == 0:
            return "?"

        return node[3]

    def get_charger(self):
        for i in self.__nodes:
            if i[3] == "u":
                return i[0], i[1]

    def charger_located(self):
        return self.get_node(self.get_charger()) == "u"

    def explore(self, position):
        self.__position = position
        self.__explore_node(position)
        self.__explore_node(self.__get_scan_zone_north())
        self.__explore_node(self.__get_scan_zone_east())
        self.__explore_node(self.__get_scan_zone_south())
        self.__explore_node(self.__get_scan_zone_west())

    def __explore_node(self, position):
        try:
            node_index = self.__get_node_index_at(position)
            self.__nodes[node_index] = self.__get_node_as_explored(node_index)

        except IndexError:
            return

    def __get_node_as_explored(self, index):
        node = self.__nodes[index]
        return node[0], node[1], 1, node[3]

    def __get_scan_zone_north(self):
        return tuple(map(sum, zip(self.__position, (-1, 0))))

    def __get_scan_zone_east(self):
        return tuple(map(sum, zip(self.__position, (0, 1))))

    def __get_scan_zone_south(self):
        return tuple(map(sum, zip(self.__position, (1, 0))))

    def __get_scan_zone_west(self):
        return tuple(map(sum, zip(self.__position, (0, -1))))