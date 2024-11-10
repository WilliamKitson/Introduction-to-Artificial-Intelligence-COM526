from charger import Charger

def test_render_default():
    assert(Charger(0, 0).render() == "u")

def test_render_east():
    charger = Charger(0, 0)
    charger.turn()

    assert(charger.render() == "l")

def test_render_south():
    charger = Charger(0, 0)
    charger.turn()
    charger.turn()

    assert(charger.render() == "d")

def test_render_west():
    charger = Charger(0, 0)
    charger.turn()
    charger.turn()
    charger.turn()

    assert(charger.render() == "r")