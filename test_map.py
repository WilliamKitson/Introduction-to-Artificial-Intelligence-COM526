from map import Map

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

def test_node_blocked():
    width = 10
    height = 10

    for i in range(0, width):
        for j in range(0, height):
            assert(Map(generate_test_map(width, height, i, j, "x")).get_blocked(i, j) == 0)

def generate_test_map(width, height, x, y, char):
    map_data = ""

    for i in range(width):
        for j in range(height):
            if (i,j) == (x,y):
                map_data += char

            else:
                map_data += '0'

        map_data += '\n'

    return map_data

def test_node_open():
    width = 10
    height = 10

    for i in range(0, width):
        for j in range(0, height):
            assert(Map(generate_test_map(width, height, i, j, " ")).get_blocked(i, j) == 1)

def test_get_start():
    width = 10
    height = 10

    for i in range(0, width):
        for j in range(0, height):
            unit = Map(generate_test_map(width, height, i, j, "^"))
            assert(unit.get_start() == (i, j))

def test_get_charger():
    width = 10
    height = 10

    for i in range(0, width):
        for j in range(0, height):
            unit = Map(generate_test_map(width, height, i, j, "u"))
            assert(unit.get_charger() == (i, j))

def test_render():
    map_data = ("qwertyiopas\n"
                "asdfghjklzx\n"
                "cvbnm123456\n")

    render = Map(map_data)
    index = 0

    for i in range(0, render.get_height()):
        for j in range(0, render.get_width()):
            if map_data[index] == "\n":
                index += 1

            assert(render.get_render(i, j) == map_data[index])
            index += 1

def test_render_start():
    assert(Map("^").get_render(0, 0) == " ")

def test_render_charger():
    assert(Map("u").get_render(0, 0) == " ")