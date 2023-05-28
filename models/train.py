from models.transport import Transport


class Train(Transport):
    def __init__(self, id=100, max_speed=0, carriage=0, quantity_of_passengers=0):
        super().__init__(id, max_speed, quantity_of_passengers)
        self.carriage = carriage

    def accelerate(self, speed):
        self.max_speed += speed

    def __str__(self):
        return f"Train (id = {self.id}, max_speed = {self.max_speed}, carriage = {self.carriage}, quantity_of_passengers = {self.quantity_of_passengers})"

