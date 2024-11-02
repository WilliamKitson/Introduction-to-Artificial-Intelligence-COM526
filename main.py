from cleaner import Cleaner

cleaner = Cleaner(0, 0)

while cleaner.get_battery():
    cleaner.set_forwards(0)
    cleaner.cycle()
    print(f"cycle {cleaner.get_cycle()}: {cleaner.get_render()} ({cleaner.get_battery()}%)")