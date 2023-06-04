from models.transport import Transport


class Car(Transport):
    def __init__(self, id=100, quantity_of_passengers=0, max_speed=0, num_doors=0, trunk_volume=0, max_load=0):
        """

        :param id (int): The identifier for the car. Defaults to 100.
        :param quantity_of_passengers (int): The number of passengers the car can hold. Defaults to 0.
        :param max_speed (int): The maximum speed of the car. Defaults to 0.
        :param num_doors (int): The number of doors the car has. Defaults to 0.
        :param trunk_volume (int): The volume of the car's trunk in liters. Defaults to 0.
        :param max_load (int): The maximum load capacity of the car in kilograms. Defaults to 0.
        """
        super().__init__(id, quantity_of_passengers, max_speed)
        self.num_doors = num_doors
        self.trunk_volume = trunk_volume
        self.max_load = max_load
        self.lock_set = {"automatic locks", "keys"}

    def accelerate(self, speed):
        """The car overrides parent class`s acceleration method"""
        self.max_speed += speed

    def refuel(self):
        """ Refuels the car """
        print("Refueling the car")

    def __str__(self):
        """Returns a string representation of the object"""
        return f"Car (id = {self.id}\f" \
               f"max_speed = {self.max_speed}\f" \
               f"num_doors = {self.num_doors}\f" \
               f"trunk_volume = {self.trunk_volume}\f" \
               f"max_load = {self.max_load}"
