class PetUserInterface:
    def ask_user_pet_info():
        pet_name = input("Enter the pet's name: ")
        pet_animal_type = input("Enter the pet's animal type: ")
        pet_age = input("Enter the pet's age: ")
        return pet_name, pet_animal_type, pet_age