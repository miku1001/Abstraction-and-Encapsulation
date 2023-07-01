# Import FanClass
from PetClass import Pet
from termcolor import colored

# Create a Test Driver program named ClassPet
class TestPet:
    def test(self):

        print("\033[1;31;40m FLEX YOUR PET \033[0m".center(80))
        print(colored(("-" * 72), color='red'))

        name = input(colored(("Enter the name of pet: "), color = "green"))
        animal_type = input(colored(("Enter the type of animal:"), color = "blue"))
        age = input(colored(("Enter the age(in years): "), color = "yellow"))

        pet = Pet(name, animal_type, age)


        # print pet details
        print(colored("=" * 72, color = "red"))
        print()
        print(f'His/Her name is \033[32m{pet.get_name()}\033[0m')
        print(f'He/She is a \033[34m{pet.get_animal_type()}\033[0m')
        print(f'He/She is \033[33m{pet.get_age()} years old\033[0m')



# __start__
test_run = TestPet()
test_run.test()