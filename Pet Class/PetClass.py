# Import ptfiglet and termcolor
from pyfiglet import Figlet
from termcolor import colored

# Create header
f = Figlet(font='banner3-D')
print(colored(f.renderText("       Pet       "), 'red'))
print(colored(("=" * 73), color='red'))

# Create class for pet
class Pet:
    # Create constructor
    # Set default name, animal type, and age
    def __init__(self, name, animal_type, age):
        # Create instance variable
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Create getter method for name
    def get_name(self):
        return self.__name
    
    # Create setter method for name
    def set_name(self, name):
        self.__name = name

    # Create getter method for animal type
    def get_animal_type(self):
        return self.__animal_type
    
    # Create setter method for animal type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Create getter method for age
    def get_age(self):
        return self.__age
    
    # Create setter method for age
    def set_age(self, age):
        self.__age = age
