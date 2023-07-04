from pet import Pet
from pet_ui import PetUserInterface

pet = Pet()
pet_name, pet_animal_type, pet_age = PetUserInterface.ask_user_pet_info()

pet.set_name(pet_name)
pet.set_animal_type(pet_animal_type)
pet.set_age(pet_age)

print("Pet's name: ", pet.get_name(pet_name))
print(f"{pet.get_name(pet_name)} is a {pet.get_animal_type(pet_animal_type)}")
print(f"{pet.get_name(pet_name)} is {pet.get_age(pet_age)} years old")