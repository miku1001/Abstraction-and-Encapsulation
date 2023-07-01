# Import ptfiglet and termcolor
from pyfiglet import Figlet
from termcolor import colored

# Create header
f = Figlet(font='banner3-D')
print(colored(f.renderText("       Fan       "), 'green'))
print(colored(("=" * 73), color='green'))

# Create class for fan
class Fan:
# Create constant for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Create constructor
    # Set default fan speed, on, radius and color
    def __init__(self, speed = SLOW, on = False, radius = 5, color = "blue"):
    # Create instance variable
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # Create getter method for fan speed
    def get_fan_speed(self):
        return self.__speed
        
    # Create setter method for fan speed
    def set_fan_speed(self, speed):
        self.__speed = speed
    
    # Create getter method for power status
    def get_on(self):
        if self.__on == True:
            return "On"
        else:
            return "Off"
        
    # Create setter method for power status
    def set_on(self, on):
        self.__on = on
    
    # Create getter method for radius
    def get_radius(self):
        return self.__radius
        
    # Create setter method for radius
    def set_radius(self, radius):
        self.__radius = radius
    
    # Create getter method for color
    def get_color(self):
        return self.__color
        
    # Create setter method for color
    def set_color(self, color):
        self.__color = color