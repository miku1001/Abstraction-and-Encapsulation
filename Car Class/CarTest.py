# Import CarClass
from CarClass import Car
from termcolor import colored

class TestCar:
    def test(self):
        print("\033[1;34;40m Car Status \033[0m".center(80))
        print(colored(("-" * 72), color='blue'))
        car = Car(2016, "Toyota", 0)
        car.accelerate()
        car.accelerate()
        car.accelerate()
        car.accelerate()
        car.accelerate()
        car.brake()
        car.brake()
        car.brake()
        car.brake()
        car.brake()

        # print car status
        print(f'Model Year: \033[32m{car.get_year()}\033[0m')
        print(f'Car Make: \033[33m{car.get_make()}\033[0m')
        print(f'Speed: \033[34m{car.get_speed()} kp/h\033[0m')

# __start__
test_run = TestCar()
test_run.test()