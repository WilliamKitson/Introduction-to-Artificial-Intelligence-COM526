from charger import Charger

def test_render_default():
    assert(Charger(0, 0).render() == "u")

def test_render_east():
    charger = Charger(0, 0)
    charger.turn()

    assert(charger.render() == "i")