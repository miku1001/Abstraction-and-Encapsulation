# Create class for fan
class Fan:
# Create constannt for fan speed
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
    
# Create getter methods for fan speed, power status, radius, and color
# Create setter methods for fan speed, power status, radius, and color