#  Copyright (c) 2024. William E. Kitson

from version_2.cleaner import Cleaner

def test_cycle_default():
    assert(Cleaner((0, 0)).get_cycle() == 0)

def test_cycle_cycling():
    cleaner = Cleaner((0, 0))

    for i in range(1, 10):
        cleaner.cycle()
        assert(cleaner.get_cycle() == i)

def test_battery_default():
    assert(Cleaner((0, 0)).get_battery() == 100)

def test_battery_turn():
    cleaner = Cleaner((0, 0))
    battery = cleaner.get_battery()

    for i in range(1, 10):
        cleaner.sense(0, 0)
        cleaner.cycle()
        assert(cleaner.get_battery() == battery - i)

def test_battery_move():
    cleaner = Cleaner((0, 0))
    battery = cleaner.get_battery()

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_battery() == battery - (i * 2))

def test_battery_clean():
    cleaner = Cleaner((0, 0))
    battery = cleaner.get_battery()

    for i in range(1, 10):
        cleaner.sense(1, 0)
        cleaner.cycle()
        assert(cleaner.get_battery() == battery - (i * 3))

def test_battery_minimum():
    cleaner = Cleaner((0, 0))

    while cleaner.get_battery() > 0:
        cleaner.sense(0, 0)
        cleaner.cycle()

    cleaner.cycle()
    assert(cleaner.get_battery() == 0)

def test_position_initialisation():
    for i in range(10):
        for j in range(10):
            assert(Cleaner((i, j)).get_position() == (i, j))

def test_move_default():
    cleaner = Cleaner((0, 0))

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_position() == (-i, 0))

def test_move_east():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_position() == (0, i))

def test_move_south():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_position() == (i, 0))

def test_move_west():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_position() == (0, -i))

def test_move_north():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_position() == (-i, 0))

def test_clean_uncleaned():
    cleaner = Cleaner((0, 0))
    cleaner.sense(1, 0)
    assert(cleaner.get_cleaned() == 1)

def test_clean_cleaned():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    assert(cleaner.get_cleaned() == 0)

def test_render_default():
    assert(Cleaner((0, 0)).get_render() == '^')

def test_render_east():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()
    assert (cleaner.get_render() == '>')

def test_render_south():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()
    cleaner.cycle()
    assert (cleaner.get_render() == 'v')

def test_render_west():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    assert (cleaner.get_render() == '<')

def test_render_north():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    assert (cleaner.get_render() == '^')

def test_uncharged_turn():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)

    while cleaner.get_battery() > 0:
        cleaner.cycle()

    cleaner.cycle()
    assert (cleaner.get_render() == "^")

def test_uncharged_forward():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 1)

    while cleaner.get_battery() > 0:
        cleaner.cycle()

    cleaner.cycle()
    assert (cleaner.get_position() == (-50, 0))

def test_recharge_maximum():
    cleaner = Cleaner((0, 0))
    cleaner.recharge(1)
    cleaner.cycle()
    assert (cleaner.get_battery() == 100)

def test_scan_default():
    cleaner = Cleaner((0, 0))

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_scan_position() == (-i - 1, 0))

def test_scan_east():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_scan_position() == (0, i + 1))

def test_scan_south():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_scan_position() == (i + 1, 0))

def test_scan_west():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_scan_position() == (0, -i - 1))

def test_scan_north():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.sense(0, 1)
        cleaner.cycle()
        assert(cleaner.get_scan_position() == (-i - 1, 0))

def test_has_path():
    cleaner = Cleaner((0, 0))
    cleaner.set_path([(0,0), (0,1)])
    assert(cleaner.has_path() == True)

def test_has_no_path():
    cleaner = Cleaner((0, 0))
    assert(cleaner.has_path() == False)

def test_path_direction_east():
    cleaner = Cleaner((0,0))
    cleaner.sense(0, 1)
    cleaner.set_path([(0,0), (0,1)])
    cleaner.cycle()
    cleaner.cycle()
    assert(cleaner.get_render() == ">")

def test_path_direction_south():
    cleaner = Cleaner((0,0))
    cleaner.sense(0, 1)
    cleaner.set_path([(0,0), (1,0)])
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    assert(cleaner.get_render() == "v")

def test_path_direction_west():
    cleaner = Cleaner((0,0))
    cleaner.sense(0, 1)
    cleaner.set_path([(0,0), (0,-1)])
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    assert(cleaner.get_render() == "<")

def test_path_direction_north():
    cleaner = Cleaner((0,0))
    cleaner.sense(0, 0)
    cleaner.cycle()

    cleaner.sense(0, 1)
    cleaner.set_path([(0,0), (-1,0)])
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    assert(cleaner.get_render() == "^")

def test_path_move_east():
    cleaner = Cleaner((0,0))
    cleaner.sense(0, 1)
    cleaner.set_path([(0,0), (0,1)])
    cleaner.cycle()
    cleaner.cycle()
    assert(cleaner.get_position() == (0,1))

def test_battery_rechargable():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)

    while cleaner.get_battery() > 0:
        cleaner.cycle()

    for i in (range(1, 75)):
        cleaner.recharge(1)
        cleaner.cycle()
        assert (cleaner.get_battery() == i)

def test_battery_unchargable():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 0)

    while cleaner.get_battery() > 76:
        cleaner.cycle()

    cleaner.recharge(25)
    cleaner.cycle()

    assert(cleaner.get_battery() == 76)

# test that cleaner will not move while charging until 100%
def test_charging_immobile():
    cleaner = Cleaner((0, 0))
    cleaner.sense(0, 1)

    while cleaner.get_battery() > 50:
        cleaner.cycle()

    cleaner.recharge(1)
    pre_charge_position = cleaner.get_position()

    for i in range(1, 50):
        cleaner.cycle()
        assert(cleaner.get_position() == pre_charge_position)