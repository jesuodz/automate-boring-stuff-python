class Vehicle:
    def __init__(self, num_of_wheels, type_tank, seats_capacity, max_velocity):
        self.num_of_wheels = num_of_wheels
        self.type_tank = type_tank
        self.seats_capacity = seats_capacity
        self.max_velocity = max_velocity
    
    @property
    def num_of_wheels(self):
        return self.__num_of_wheels

    @num_of_wheels.setter
    def num_of_wheels(self, number):
        self.__num_of_wheels = number

tesla_model_s = Vehicle(4, 'electric', 5, 250)
print(tesla_model_s.num_of_wheels)
tesla_model_s.num_of_wheels = 2
print(tesla_model_s.num_of_wheels)
