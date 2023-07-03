class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed = slow, radius = 5, color = "blue", power = False):
        self.__speed = speed
        self.__power = power
        self.__radius = radius
        self.__color = color