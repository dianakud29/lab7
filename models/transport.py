from abc import ABC, abstractmethod


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

    @abstractmethod
    def accelerate(self, speed):
        """Abstract method to accelerate the transport"""
        pass

    @abstractmethod
    def refuel(self):
        """Abstract method to refuel the transport"""
        pass

    def __iter__(self):
        """Returns an iterator for the lock set"""
        return iter(self.lock_set)
