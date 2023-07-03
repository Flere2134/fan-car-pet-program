class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed = slow, radius = 5, color = "blue", power = False):
        self.__speed = speed
        self.__power = power
        self.__radius = radius
        self.__color = color

    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
    def get_power(self):
        return self.__power
    def set_power(self, power):
        self.__power = power