#  Copyright (c) 2024. William E. Kitson

from version_2.local_knowledge import LocalKnowledge

def test_empty_node():
    pathfinder = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            assert(pathfinder.get_node((i, j)) == "?")

def test_explored_free():
    pathfinder = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            pathfinder.add_free((i, j))
            pathfinder.explore((i, j))
            assert(pathfinder.get_node((i, j)) == " ")

def test_unexplored_free():
    pathfinder = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            pathfinder.add_free((i, j))
            assert(pathfinder.get_node((i, j)) == "?")

def test_explored_blocked():
    pathfinder = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            pathfinder.add_blocked((i, j))
            pathfinder.explore((i, j))
            assert(pathfinder.get_node((i, j)) == "x")

def test_unexplored_blocked():
    pathfinder = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            pathfinder.add_blocked((i, j))
            assert(pathfinder.get_node((i, j)) == "?")

def test_scan_zone_north():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = LocalKnowledge()
            position_north = tuple(map(sum, zip((i, j), (-1, 0))))

            pathfinder.add_free(position_north)
            pathfinder.explore((i, j))
            assert(pathfinder.get_node(position_north) == " ")

def test_scan_zone_east():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = LocalKnowledge()
            position_east = tuple(map(sum, zip((i, j), (0, 1))))

            pathfinder.add_free(position_east)
            pathfinder.explore((i, j))
            assert(pathfinder.get_node(position_east) == " ")

def test_scan_zone_south():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = LocalKnowledge()
            position_south = tuple(map(sum, zip((i, j), (1, 0))))

            pathfinder.add_free(position_south)
            pathfinder.explore((i, j))
            assert(pathfinder.get_node(position_south) == " ")

def test_scan_zone_west():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = LocalKnowledge()
            position_west = tuple(map(sum, zip((i, j), (0, -1))))

            pathfinder.add_free(position_west)
            pathfinder.explore((i, j))
            assert(pathfinder.get_node(position_west) == " ")