from models.transport import Transport


class Car(Transport):
    def __init__(self, id=100, quantity_of_passengers = 0, max_speed=0, num_doors=0, trunk_volume=0, max_load=0):
        super().__init__(id, quantity_of_passengers, max_speed)
        self.num_doors = num_doors
        self.trunk_volume = trunk_volume
        self.max_load = max_load

    def accelerate(self, speed):
        self.max_speed += speed

    def __str__(self):
        return f"Car (id = {self.id}, max_speed = {self.max_speed}, num_doors = {self.num_doors}, trunk_volume = {self.trunk_volume}, max_load = {self.max_load})"
