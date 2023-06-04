from models.transport import Transport


class Trolleybus(Transport):
    """Description of the trolleybus"""

    __instance = None

    def __init__(self, id=100, quantity_of_passengers=0, route_number=0, current_stop="", max_speed=0, capacity=0,
                 passengers=0):
        """

        :param id (int): id of trolleybus.Defaults to 100.
        :param route_number (int): number of each trolleybus.Defaults to 0.
        :param current_stop (str): current stop where is trolleybus stop.Defaults to an empty string.
        :param max_speed (int): max speed of trolleybus. Defaults to 0.
        :param capacity (int): capacity of trolleybus. Defaults to 0.
        :param passengers (int): max quantity of passengers. Defaults to 0.
        """
        super().__init__(id, quantity_of_passengers, max_speed)
        self.id = 100
        self.quantity_of_passengers = quantity_of_passengers
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed = max_speed
        self.capacity = capacity
        self.passengers = passengers
        self.lock_set = {"mechanical locks", "electronic locks"}

    def accelerate(self, speed):
        """The trolleybus overrides parent class`s acceleration method"""
        self.max_speed += speed

    def refuel(self):
        """ Refuels the trolleybus """
        print("Refueling the trolleybus")

    def stop(self):
        """The trolleybus stops"""
        self.max_speed = 0

    def start(self):
        """The trolleybus has the current speed"""
        self.max_speed = 20

    def add_passenger(self):
        """Adding 1 passenger to the trolleybus"""
        if self.passengers < self.capacity:
            self.passengers += 1

    def remove_passenger(self):
        """Removal of 1 passenger"""
        if self.passengers > 0:
            self.passengers -= 1

    def __str__(self):
        """Returns a string representation of the object"""
        return f"Trolleybus (id = {self.id}\f" \
               f"route_number = {self.route_number}\f" \
               f"current_stop = {self.current_stop}\f" \
               f"max_speed = {self.max_speed}\f" \
               f"capacity = {self.capacity}\f" \
               f"passengers = {self.passengers}"
