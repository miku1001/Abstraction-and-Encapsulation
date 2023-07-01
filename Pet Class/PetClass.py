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
    # Create setter method for animal type
    # Create getter method for age
    # Create setter method for age