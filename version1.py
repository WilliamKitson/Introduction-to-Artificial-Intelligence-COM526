from cleaner import Cleaner

class Version1:
    def __init__(self):
        self.__cleaner = Cleaner(0, 0)

    def execute(self):
        while self.__cleaner.get_battery():
            self.__cleaner.set_forwards(0)
            self.__cleaner.cycle()
            print(f"cycle {self.__cleaner.get_cycle()}: {self.__cleaner.get_render()} ({self.__cleaner.get_battery()}%)")