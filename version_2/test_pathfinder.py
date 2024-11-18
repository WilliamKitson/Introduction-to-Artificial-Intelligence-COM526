from version_2.Pathfinder import Pathfinder

def test_explored_free():
    pathfinder = Pathfinder()

    for i in range(1, 10):
        for j in range(1, 10):
            pathfinder.add_free((i, j))
            pathfinder.set_position((i, j))
            assert(pathfinder.get_node((i, j)) == " ")

def test_unexplored_free():
    pathfinder = Pathfinder()

    for i in range(1, 10):
        for j in range(1, 10):
            pathfinder.add_free((i, j))
            assert(pathfinder.get_node((i, j)) == "?")

def test_explored_blocked():
    pathfinder = Pathfinder()

    for i in range(1, 10):
        for j in range(1, 10):
            pathfinder.add_blocked((i, j))
            pathfinder.set_position((i, j))
            assert(pathfinder.get_node((i, j)) == "x")

def test_scan_zone_north():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = Pathfinder()
            pathfinder.set_position((i, j))
            assert(pathfinder.get_scan_zone_north() == (i - 1, j))

def test_scan_zone_east():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = Pathfinder()
            pathfinder.set_position((i, j))
            assert(pathfinder.get_scan_zone_east() == (i, j + 1))

def test_scan_zone_south():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = Pathfinder()
            pathfinder.set_position((i, j))
            assert(pathfinder.get_scan_zone_south() == (i + 1, j))

def test_scan_zone_west():
    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder = Pathfinder()
            pathfinder.set_position((i, j))
            assert(pathfinder.get_scan_zone_west() == (i, j - 1))