from version_2.Pathfinder import Pathfinder

def test_render_default():
    start = (0, 0)
    assert(Pathfinder(start).render(start) == " ")