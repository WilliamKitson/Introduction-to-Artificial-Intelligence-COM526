from cleaner import Cleaner

cleaner = Cleaner(0, 0)

for i in range(10):
    cleaner.set_forwards(0)
    cleaner.cycle()
    print(f"cycle {cleaner.get_cycle()}: {cleaner.get_render()} ({cleaner.get_battery()}%)")