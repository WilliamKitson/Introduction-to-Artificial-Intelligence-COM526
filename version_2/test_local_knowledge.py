#  Copyright (c) 2024. William E. Kitson

from version_2.local_knowledge import LocalKnowledge

def test_empty_node():
    local_knowledge = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            assert(local_knowledge.get_node((i, j)) == "?")

def test_explored_free():
    local_knowledge = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            local_knowledge.add_free((i, j), (i + j))
            local_knowledge.explore((i, j))
            assert(local_knowledge.get_node((i, j)) == str(i + j))

def test_unexplored_free():
    local_knowledge = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            local_knowledge.add_free((i, j), (i + j))
            assert(local_knowledge.get_node((i, j)) == "?")

def test_explored_blocked():
    local_knowledge = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            local_knowledge.add_blocked((i, j))
            local_knowledge.explore((i, j))
            assert(local_knowledge.get_node((i, j)) == "x")

def test_unexplored_blocked():
    local_knowledge = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            local_knowledge.add_blocked((i, j))
            assert(local_knowledge.get_node((i, j)) == "?")

def test_explored_charger():
    local_knowledge = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            local_knowledge.add_charger((i, j))
            local_knowledge.explore((i, j))
            assert(local_knowledge.get_node((i, j)) == "u")

def test_unexplored_charger():
    local_knowledge = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            local_knowledge.add_charger((i, j))
            assert(local_knowledge.get_node((i, j)) == "?")

def test_scan_zone_north():
    for i in range(0, 10):
        for j in range(0, 10):
            local_knowledge = LocalKnowledge()
            position_north = tuple(map(sum, zip((i, j), (-1, 0))))

            local_knowledge.add_free(position_north, (i + j))
            local_knowledge.explore((i, j))
            assert(local_knowledge.get_node(position_north) == str(i + j))

def test_scan_zone_east():
    for i in range(0, 10):
        for j in range(0, 10):
            local_knowledge = LocalKnowledge()
            position_east = tuple(map(sum, zip((i, j), (0, 1))))

            local_knowledge.add_free(position_east, (i + j))
            local_knowledge.explore((i, j))
            assert(local_knowledge.get_node(position_east) == str(i + j))

def test_scan_zone_south():
    for i in range(0, 10):
        for j in range(0, 10):
            local_knowledge = LocalKnowledge()
            position_south = tuple(map(sum, zip((i, j), (1, 0))))

            local_knowledge.add_free(position_south, (i + j))
            local_knowledge.explore((i, j))
            assert(local_knowledge.get_node(position_south) == str(i + j))

def test_scan_zone_west():
    for i in range(0, 10):
        for j in range(0, 10):
            local_knowledge = LocalKnowledge()
            position_west = tuple(map(sum, zip((i, j), (0, -1))))

            local_knowledge.add_free(position_west, (i + j))
            local_knowledge.explore((i, j))
            assert(local_knowledge.get_node(position_west) == str(i + j))

def test_get_charger():
    for i in range(1, 10):
        for j in range(1, 10):
            local_knowledge = LocalKnowledge()
            local_knowledge.add_charger((i, j))
            assert (local_knowledge.get_charger() == (i, j))

def test_charger_located():
    local_knowledge = LocalKnowledge()
    local_knowledge.add_charger((0, 0))
    local_knowledge.explore((0, 0))

    assert(local_knowledge.charger_located() == True)

def test_charger_undiscovered():
    local_knowledge = LocalKnowledge()
    local_knowledge.add_charger((0, 0))

    assert(local_knowledge.charger_located() == False)

def test_update_free():
    local_knowledge = LocalKnowledge()

    for i in range(1, 10):
        for j in range(1, 10):
            local_knowledge.add_free((i, j), 0)
            local_knowledge.explore((i, j))
            local_knowledge.update_free((i, j), (i + j))

            assert(local_knowledge.get_node((i, j)) == str(i + j))

# test you cannot update non free nodes

# test node queue prioretises the highest dirt value
# test node queue prioretises unexplored when no dirt is detcted