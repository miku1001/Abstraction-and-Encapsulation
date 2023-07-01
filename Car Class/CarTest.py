# Import CarClass
from CarClass import Car
from termcolor import colored

class TestCar:
    def test(self):
        print("\033[1;33;40m Car Status \033[0m".center(80))
        print(colored(("-" * 72), color='blue'))


# __start__
test_run = TestCar()
test_run.test()