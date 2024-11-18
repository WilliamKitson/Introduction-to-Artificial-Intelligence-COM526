from version_2.Pathfinder import Pathfinder

def test_add_node():
    pathfinder = Pathfinder((0, 0))

    for i in range(0, 10):
        for j in range(0, 10):
            pathfinder.add_node((i, j, i + j))
            assert(pathfinder.get_node((i, j)) == i + j)

def test_render_default():
    start = (0, 0)
    assert(Pathfinder(start).render(start) == " ")

def test_render_unexplored():
    assert(Pathfinder((0, 0)).render((1, 0)) == "?")