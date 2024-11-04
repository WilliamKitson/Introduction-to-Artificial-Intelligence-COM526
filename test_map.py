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
            assert(Map(generate_test_map(width, height, i, j, "x")).get_blocked(i, j) == True)

def test_node_open():
    width = 10
    height = 10

    for i in range(0, width):
        for j in range(0, height):
            assert(Map(generate_test_map(width, height, i, j, " ")).get_blocked(i, j) == False)

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