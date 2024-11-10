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

def test_render_north():
    charger = Charger(0, 0)
    charger.turn()
    charger.turn()
    charger.turn()
    charger.turn()

    assert(charger.render() == "u")

def test_position():
    for i in range(0, 5):
        assert(Charger(i, i + 1).get_position() == (i, i + 1))

def test_charge():
    assert(Charger(0, 0).get_charge() == 5)

def test_charge_zone_default():
    for i in range(0, 5):
        assert(Charger(i, -i).get_charge_zone() == (i + 1, -i))

def test_charge_zone_east():
    for i in range(0, 5):
        charger = Charger(-i, i)
        charger.turn()

        assert(charger.get_charge_zone() == (-i, i + 1))

def test_charge_zone_south():
    for i in range(0, 5):
        charger = Charger(i, -i)
        charger.turn()
        charger.turn()

        assert(charger.get_charge_zone() == (i - 1, -i))