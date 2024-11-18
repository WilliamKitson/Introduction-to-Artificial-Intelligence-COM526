from version_2.local_knowledge import LocalKnowledge

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
            pathfinder.add_free((i, j))
            pathfinder.explore((i, j))
            assert(pathfinder.get_scan_zone_north() == (i - 1, j))

def test_scan_zone_east():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = LocalKnowledge()
            pathfinder.add_free((i, j))
            pathfinder.explore((i, j))
            assert(pathfinder.get_scan_zone_east() == (i, j + 1))

def test_scan_zone_south():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = LocalKnowledge()
            pathfinder.add_free((i, j))
            pathfinder.explore((i, j))
            assert(pathfinder.get_scan_zone_south() == (i + 1, j))

def test_scan_zone_west():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = LocalKnowledge()
            pathfinder.add_free((i, j))
            pathfinder.explore((i, j))
            assert(pathfinder.get_scan_zone_west() == (i, j - 1))