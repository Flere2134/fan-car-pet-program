class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = ''
        self.__animal_type = ''
        self.__age = ''
    def set_name(self, name):
        self.__name = name
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    def set_age(self, age):
        self.__age = age