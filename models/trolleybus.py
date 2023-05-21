from models.transport import Transport


class Trolleybus(Transport):
    """Description of the trolleybus"""

    __instance = None

    def __init__(self, id=100, quantity_of_passengers = 0, route_number=0, current_stop="", max_speed=0, capacity=0, passengers=0):
        """

        :param id: id of trolleybus
        :param route_number: number of each trolleybus
        :param current_stop: current stop where is trolleybus stop
        :param max_speed: max speed of trolleybus
        :param capacity: capacity of trolleybus
        :param passengers: max quantity of passengers
        """
        super().__init__(id, quantity_of_passengers, max_speed)
        self.id = 100
        self.quantity_of_passengers = quantity_of_passengers
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed = max_speed
        self.capacity = capacity
        self.passengers = passengers

    def accelerate(self, speed):
        self.max_speed += speed

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


