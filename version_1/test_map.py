#  Copyright (c) 2024. William E. Kitson

from version_1.map import Map

def test_map_width():
    map_data = ""

    for i in range(1, 10):
        map_data += 'x'
        assert(Map(map_data).get_width() == i)

def test_map_height():
    map_data = ""

    for i in range(1, 10):
        map_data += '\n'
        assert(Map(map_data).get_height() == i)

def test_blocked_wall():
    width = 10
    height = 5

    for i in range(0, width):
        for j in range(0, height):
            assert(Map(generate_test_map(width, height, i, j, "x")).get_blocked((i, j)) == 0)

def test_blocked_charger():
    width = 10
    height = 5

    for i in range(0, width):
        for j in range(0, height):
            assert(Map(generate_test_map(width, height, i, j, "u")).get_blocked((i, j)) == 0)

def generate_test_map(width, height, x, y, char):
    map_data = ""

    for j in range(height):
        for i in range(width):
            if (i,j) == (x,y):
                map_data += char

            else:
                map_data += '0'

        map_data += '\n'

    return map_data

def test_node_open():
    width = 10
    height = 5

    for i in range(0, width):
        for j in range(0, height):
            assert(Map(generate_test_map(width, height, i, j, " ")).get_blocked((i, j)) == 1)

def test_dirt_range():
    loaded_map = Map(("     \n"
                      "     "))

    for i in range(0, loaded_map.get_width()):
        for j in range(0, loaded_map.get_height()):
            assert(loaded_map.get_dirt((i, j)) in range(0, 9))

def test_dirt_random():
    map_data = ("     \n"
                "     ")

    assert(get_dirt_sum_total(Map(map_data)) != get_dirt_sum_total(Map(map_data)))

def get_dirt_sum_total(loaded_map):
    sum_total = 0

    for i in range(0, loaded_map.get_width()):
        for j in range(0, loaded_map.get_height()):
            sum_total += loaded_map.get_dirt((i, j))

    return sum_total

def test_dirt_consistent():
    loaded_map = Map(("     \n"
                      "     "))

    assert(get_dirt_sum_total(loaded_map) == get_dirt_sum_total(loaded_map))

def test_dirt_invalid():
    loaded_map = Map(("x^u\n"
                      "x^u"))

    assert (get_dirt_sum_total(loaded_map) == 0)

def test_dirt_set():
    loaded_map = Map(("     \n"
                      "     "))

    for i in range(0, loaded_map.get_width()):
        for j in range(0, loaded_map.get_height()):
            cleaned = i + j
            loaded_map.set_dirt((i, j), cleaned)
            assert(loaded_map.get_dirt((i, j)) == cleaned)

def test_get_start():
    width = 10
    height = 5

    for i in range(0, width):
        for j in range(0, height):
            unit = Map(generate_test_map(width, height, i, j, "^"))
            assert(unit.get_start() == (i, j))

def test_get_charger():
    width = 10
    height = 5

    for i in range(0, width):
        for j in range(0, height):
            unit = Map(generate_test_map(width, height, i, j, "u"))
            assert(unit.get_charger() == (i, j))

def test_valid_render():
    map_data = ("xxxxxxxxxx\n"
                "xxxxxxxxxx\n"
                "xxxxxxxxxx\n")

    render = Map(map_data)
    index = 0

    for i in range(0, render.get_width()):
        for j in range(0, render.get_height()):
            if map_data[index] == "\n":
                index += 1

            assert(render.get_render((i, j)) == "x")
            index += 1

def test_invalid_render():
    map_data = ("123vu123vu\n"
                "123vu123vu\n"
                "123vu123vu\n")

    render = Map(map_data)
    index = 0

    for i in range(0, render.get_width()):
        for j in range(0, render.get_height()):
            if map_data[index] == "\n":
                index += 1

            assert(render.get_render((i, j)) == " ")
            index += 1