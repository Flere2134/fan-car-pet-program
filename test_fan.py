from fan import Fan

class TestFan:
    def main(self):
        fan_num_1 = Fan(Fan.fast, 10, "yellow", True)
        fan_num_2 = Fan(Fan.medium, 5, "blue", False)
    
        print("Fan 1 speed is", fan_num_1.get_speed())
        print("Fan 1 radius is", fan_num_1.get_radius())
        print("Fan 1 color is", fan_num_1.get_color())
        print("Fan 1 is turned on", fan_num_1.get_power())
        print("Fan 2 speed is", fan_num_2.get_speed())
        print("Fan 2 radius is", fan_num_2.get_radius())
        print("Fan 2 color is", fan_num_2.get_color())
        print("Fan 2 is turned on", fan_num_2.get_power())