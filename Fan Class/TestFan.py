# Import FanClass
from FanClass import Fan
from termcolor import colored

# Create a Test Driver program named FanClass
class TestTV:
    def test(self):
        print("\032[1;31;40m Fan1 Status \033[0m".center(80))
        print(colored(("-" * 72), color='green'))



        print("\032[1;31;40m Fan2 Status \033[0m".center(80))
        print(colored(("-" * 72), color='green'))
    