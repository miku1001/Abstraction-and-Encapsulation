# Import FanClass
from FanClass import Fan
from termcolor import colored

# Create a Test Driver program named FanClass
class TestFan:
    def test(self):
        # fan1
        print("\033[1;32;40m Fan1 Status \033[0m".center(80))
        print(colored(("-" * 72), color='green'))
        
        # create object for fan1
        fan1 = Fan(Fan.SLOW, True, 10, "yellow")
        # print
        print("\033[1;33mFan Speed:\033[0m", fan1.get_fan_speed())
        print("\033[1;31mPower:\033[0m", fan1.get_on())
        print("\033[1;34mRadius:\033[0m", fan1.get_radius())
        print("\033[1;36mColor:\033[0m", fan1.get_color())



        # fan 2
        print("\033[1;32;40m Fan2 Status \033[0m".center(80))
        print(colored(("-" * 72), color='green'))

        # create object for fan2
        fan2 = Fan(Fan.MEDIUM, False, 5, "blue")
        # print
        print("\033[1;33mFan Speed:\033[0m", fan2.get_fan_speed())
        print("\033[1;31mPower:\033[0m", fan2.get_on())
        print("\033[1;34mRadius:\033[0m", fan2.get_radius())
        print("\033[1;36mColor:\033[0m", fan2.get_color())

    

# __start__
test_run = TestFan()
test_run.test()