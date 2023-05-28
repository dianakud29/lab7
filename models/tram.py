from models.transport import Transport


class Tram(Transport):
    def __init__(self, id=100, max_speed=0, seating=0, quantity_of_passengers=0):
        """

        :param id(int): The identifier for the train. Defaults to 100.
        :param max_speed(int): The maximum speed of the train. Defaults to 0.
        :param seating(int): The maximum number of seats. Defaults 0.
        :param quantity_of_passengers(int): The total quantity of passengers the train can accommodate. Defaults to 0.
        """
        super().__init__(id, max_speed, quantity_of_passengers)
        self.seating = seating
        self.lock_set = {"trunk locks", "metal padlock"}

    def accelerate(self, speed):
        """The tram overrides parent class`s acceleration method"""
        self.max_speed += speed

    def refuel(self):
        """ Refuels the tram """
        print("Refueling the tram")

    def __str__(self):
        """Returns a string representation of the object"""
        return f"Tram (id = {self.id}\f" \
               f"max_speed = {self.max_speed}\f" \
               f"seating = {self.seating}\f" \
               f"quantity_of_passengers = {self.quantity_of_passengers})"
