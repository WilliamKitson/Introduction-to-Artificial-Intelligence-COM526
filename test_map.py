from map import Map

def test_map_width():
    map_data = ""

    for i in range(1, 10):
        map_data += 'x'
        assert(Map(map_data).get_width() == i)