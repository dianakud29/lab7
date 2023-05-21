from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, id=0, max_speed=0, quantity_of_passengers=0):
        self.id = id
        self.max_speed = max_speed
        self.quantity_of_passengers = quantity_of_passengers

    @abstractmethod
    def accelerate(self, speed):
        pass
