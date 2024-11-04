from cleaner import  Cleaner

def test_cycle_default():
    assert(Cleaner(0, 0).get_cycle() == 0)

def test_cycle_cycling():
    cleaner = Cleaner(0, 0)

    for i in range(1, 10):
        cleaner.cycle()
        assert(cleaner.get_cycle() == i)

def test_battery_default():
    assert(Cleaner(0, 0).get_battery() == 100)

def test_battery_turn():
    cleaner = Cleaner(0, 0)
    battery = cleaner.get_battery()

    for i in range(1, 10):
        cleaner.set_scan(0)
        cleaner.cycle()
        assert(cleaner.get_battery() == battery - i)

def test_battery_move():
    cleaner = Cleaner(0, 0)
    battery = cleaner.get_battery()

    for i in range(1, 10):
        cleaner.set_scan(1)
        cleaner.cycle()
        assert(cleaner.get_battery() == battery - (i * 2))

def test_battery_minimum():
    cleaner = Cleaner(0, 0)

    while cleaner.get_battery() > 0:
        cleaner.set_scan(0)
        cleaner.cycle()

    cleaner.cycle()
    assert(cleaner.get_battery() == 0)

def test_position_initialisation():
    for i in range(10):
        for j in range(10):
            assert(Cleaner(i, j).get_position() == (i, j))

def test_move_default():
    cleaner = Cleaner(0, 0)

    for i in range(1, 10):
        cleaner.set_scan(1)
        cleaner.cycle()
        assert(cleaner.get_position() == (i, 0))

def test_move_east():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_scan(1)
        cleaner.cycle()
        assert(cleaner.get_position() == (0, i))

def test_move_south():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_scan(1)
        cleaner.cycle()
        assert(cleaner.get_position() == (-i, 0))

def test_move_west():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_scan(1)
        cleaner.cycle()
        assert(cleaner.get_position() == (0, -i))

def test_move_north():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_scan(1)
        cleaner.cycle()
        assert(cleaner.get_position() == (i, 0))

def test_render_default():
    assert(Cleaner(0, 0).get_render() == '^')

def test_render_east():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()
    assert (cleaner.get_render() == '>')

def test_render_south():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()
    cleaner.cycle()
    assert (cleaner.get_render() == 'v')

def test_render_west():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    assert (cleaner.get_render() == '<')

def test_render_north():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    assert (cleaner.get_render() == '^')

def test_uncharged_turn():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)

    while cleaner.get_battery() > 0:
        cleaner.cycle()

    cleaner.cycle()
    assert (cleaner.get_render() == "^")

def test_uncharged_forward():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(1)

    while cleaner.get_battery() > 0:
        cleaner.cycle()

    cleaner.cycle()
    assert (cleaner.get_position() == (50, 0))

def test_recharge_uncharged():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)

    while cleaner.get_battery() > 0:
        cleaner.cycle()

    for i in (range(1, 100)):
        cleaner.recharge(1)
        assert (cleaner.get_battery() == i)

def test_recharge_maximum():
    cleaner = Cleaner(0, 0)
    cleaner.recharge(1)
    assert (cleaner.get_battery() == 100)

def test_scan_default():
    cleaner = Cleaner(0, 0)

    for i in range(1, 10):
        cleaner.set_scan(1)
        cleaner.cycle()
        assert(cleaner.get_scan() == (i + 1, 0))

def test_scan_east():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_scan(1)
        cleaner.cycle()
        assert(cleaner.get_scan() == (0, i + 1))

def test_scan_south():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_scan(1)
        cleaner.cycle()
        assert(cleaner.get_scan() == (-i - 1, 0))

def test_scan_west():
    cleaner = Cleaner(0, 0)
    cleaner.set_scan(0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_scan(1)
        cleaner.cycle()
        assert(cleaner.get_scan() == (0, -i - 1))