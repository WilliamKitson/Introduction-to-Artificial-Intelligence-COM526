from version_2.Pathfinder import Pathfinder

def test_add_node():
    pathfinder = Pathfinder((0, 0))

    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder.add_node((i, j, i + j))
            assert(pathfinder.get_node((i, j)) == i + j)

def test_scan_zone_north():
    for i in range(0, 10):
        for j in range(0, 10):
            assert(Pathfinder((i, j)).get_scan_zone_north() == (i - 1, j))