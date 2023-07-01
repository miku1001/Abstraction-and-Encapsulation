# Import FanClass
from FanClass import Fan
from termcolor import colored

# Create a Test Driver program named FanClass
class TestTV:
    def test(self):
        print("\033[1;31;40m Fan Status \033[0m".center(80))
        print(colored(("-" * 72), color='red'))
    