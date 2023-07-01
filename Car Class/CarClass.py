# Create class for fan
class Car:
    # Create constructor
    # Set default speed
    def __init__(self, year, make, speed = 0 ):
        # Create instance variable
        self.__year = year
        self.__make = make
        self.__speed = speed

    # Create getter methods for year, make, and speed
    def get_year(self):
        return self.__year
    
    def get_make(self):
        return self.__make
    
    def get_speed(self):
        return self.__speed

    # Create setter methods for, year, make and speed
    def set_year(self, year):
        self.__year = year
    
    def set_make(self, make):
        self.__make = make
    
    def set_speed(self, speed):
        self.__speed = speed
