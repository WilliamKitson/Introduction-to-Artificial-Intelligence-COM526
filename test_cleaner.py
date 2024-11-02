from cleaner import  Cleaner

def test_cycle_default_count():
    assert(Cleaner(0, 0).get_cycle() == 0)

def test_cycle_cycling_count():
    cleaner = Cleaner(0, 0)

    for i in range(1, 10):
        cleaner.cycle()
        assert(cleaner.get_cycle() == i)

def test_battery_default_charge():
    assert(Cleaner(0, 0).get_battery() == 100)

def test_battery_turn_left():
    cleaner = Cleaner(0, 0)
    battery = cleaner.get_battery()

    for i in range(1, 10):
        cleaner.set_forwards(0)
        cleaner.cycle()
        assert(cleaner.get_battery() == battery - i)

def test_battery_forwards():
    cleaner = Cleaner(0, 0)
    battery = cleaner.get_battery()

    for i in range(1, 10):
        cleaner.set_forwards(1)
        cleaner.cycle()
        assert(cleaner.get_battery() == battery - (i * 2))

def test_position_initialisation():
    for i in range(10):
        for j in range(10):
            assert(Cleaner(i, j).get_position() == (i, j))

def test_position_forwards_default():
    cleaner = Cleaner(0, 0)

    for i in range(1, 10):
        cleaner.set_forwards(1)
        cleaner.cycle()
        assert(cleaner.get_position() == (i, 0))

def test_position_forwards_east():
    cleaner = Cleaner(0, 0)
    cleaner.set_forwards(0)
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_forwards(1)
        cleaner.cycle()
        assert(cleaner.get_position() == (0, i))

def test_position_forwards_south():
    cleaner = Cleaner(0, 0)
    cleaner.set_forwards(0)
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_forwards(1)
        cleaner.cycle()
        assert(cleaner.get_position() == (-i, 0))

def test_position_forwards_west():
    cleaner = Cleaner(0, 0)
    cleaner.set_forwards(0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_forwards(1)
        cleaner.cycle()
        assert(cleaner.get_position() == (0, -i))

def test_position_forwards_north():
    cleaner = Cleaner(0, 0)
    cleaner.set_forwards(0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()

    for i in range(1, 10):
        cleaner.set_forwards(1)
        cleaner.cycle()
        assert(cleaner.get_position() == (i, 0))

def test_render_default():
    assert(Cleaner(0, 0).get_render() == '^')

def test_render_east():
    cleaner = Cleaner(0, 0)
    cleaner.set_forwards(0)
    cleaner.cycle()
    assert (cleaner.get_render() == '>')

def test_render_south():
    cleaner = Cleaner(0, 0)
    cleaner.set_forwards(0)
    cleaner.cycle()
    cleaner.cycle()
    assert (cleaner.get_render() == 'v')

def test_render_west():
    cleaner = Cleaner(0, 0)
    cleaner.set_forwards(0)
    cleaner.cycle()
    cleaner.cycle()
    cleaner.cycle()
    assert (cleaner.get_render() == '<')