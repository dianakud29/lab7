from models.transport import Transport


class Tram(Transport):
    def __init__(self, id=100, max_speed=0, seating=0, quantity_of_passengers=0):
        super().__init__(id, max_speed, quantity_of_passengers)
        self.seating = seating

    def accelerate(self, speed):
        self.max_speed += speed

    def __str__(self):
        return f"Tram (id = {self.id}, max_speed = {self.max_speed}, seating = {self.seating}, quantity_of_passengers = {self.quantity_of_passengers})"
