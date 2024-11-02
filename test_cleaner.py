from cleaner import  Cleaner

def test_battery_default_charge():
    assert(Cleaner(0, 0).get_battery() == 100)

def test_position_initialisation():
    for i in range(10):
        for j in range(10):
            assert(Cleaner(i, j).get_position() == (i, j))