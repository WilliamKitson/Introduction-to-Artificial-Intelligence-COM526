from charger import Charger

def test_render_default():
    assert(Charger(0, 0).render() == "u")