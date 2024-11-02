from cleaner import  Cleaner

def test_battery_default_charge():
    assert(Cleaner().get_battery() == 100)