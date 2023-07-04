from car import Car

car = Car("2023", "Nissan")

for i in range(5):
    car.accelerator()
    print("\nCar is accelerating. Showing current speed:", car.get_speed())

for i in range(5):
    car.brake()
    print("\nCar is slowly losing speed. Showing current speed:", car.get_speed())