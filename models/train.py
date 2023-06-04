from models.transport import Transport


class Train(Transport):
    def __init__(self, id=100, max_speed=0, carriage=0, quantity_of_passengers=0):
        """

        :param id(int): The identifier for the train. Defaults to 100.
        :param max_speed(int): The maximum speed of the train. Defaults to 0.
        :param carriage(int): The number of carriages the train has. Defaults to 0.
        :param quantity_of_passengers(int): The total quantity of passengers the train can accommodate. Defaults to 0.
        """
        super().__init__(id, max_speed, quantity_of_passengers)
        self.carriage = carriage
        self.lock_set = {"steering wheel locks", "front wheel locks"}

    def accelerate(self, speed):
        """The train overrides parent class`s acceleration method"""
        self.max_speed += speed

    def refuel(self):
        """ Refuels the train """
        print("Refueling the train")

    def __str__(self):
        """Returns a string representation of the object"""
        return f"Train (id = {self.id}\f" \
               f"max_speed = {self.max_speed}\f" \
               f"carriage = {self.carriage}\f" \
               f"quantity_of_passengers = {self.quantity_of_passengers}"
