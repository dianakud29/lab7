from abc import ABC, abstractmethod
from decorators.decorators import logged
from exceptions.redundant_refuel_exception import RedundantRefuelException


class Transport(ABC):
    def __init__(self, id=0, max_speed=0, quantity_of_passengers=0):
        """

        :param id(int): The identifier for the transport. Defaults to 0.
        :param max_speed(int): The maximum speed of the transport. Defaults to 0.
        :param quantity_of_passengers(int): The number of passengers on the transport. Defaults to 0.
        """
        self.id = id
        self.max_speed = max_speed
        self.quantity_of_passengers = quantity_of_passengers
        self.lock_set = set()
        self.fuel_level = 0
        self.max_fuel_capacity = 0

    @abstractmethod
    def accelerate(self, speed):
        """Abstract method to accelerate the transport"""
        pass

    @logged(RedundantRefuelException, "console")
    def refuel(self, amount):
        if self.fuel_level + amount > self.max_fuel_capacity:
            raise RedundantRefuelException()
        else:
            self.fuel_level += amount

    def __iter__(self):
        """Returns an iterator for the lock set"""
        return iter(self.lock_set)
