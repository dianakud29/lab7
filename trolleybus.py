class Trolleybus:
    """Опис тролейбуса"""

    instance = None

    def __init__(self, id=100, routeNumber=0, currentStop="", maxSpeed=0, capacity=0, passengers=0):
        self.id = 100
        self.routeNumber = routeNumber
        self.currentStop = currentStop
        self.maxSpeed = maxSpeed
        self.capacity = capacity
        self.passengers = passengers

        @property
        def id(self):
            return self.__id

        @property
        def routeNumber(self):
            return self.__routeNumber

        @property
        def currentStop(self):
            return self.__currentStop

        @property
        def maxSpeed(self):
            return self.__maxSpeed

        @property
        def capacity(self):
            return self.__capacity

        @property
        def passengers(self):
            return self.__passengers

        @id.setter
        def id(self, id):
            self.__id = id

        @routeNumber.setter
        def routeNumber(self, routeNumber):
            self.__routeNumber = routeNumber

        @currentStop.setter
        def currentStop(self, currentStop):
            self.__currentStop = currentStop

        @maxSpeed.setter
        def maxSpeed(self, maxSpeed):
            self.__maxSpeed = maxSpeed

        @capacity.setter
        def capacity(self, capacity):
            self.__capacity = capacity

        @passengers.setter
        def passengers(self, passengers):
            self.__passengers = passengers

    def stop(self):
        """Тролейбус зупиняється"""
        self.maxSpeed = 0

    def start(self):
        """Тролейбус має поточну швидкість"""
        self.maxSpeed = 20

    def addPassenger(self):
        """Додавання 1 пасажира в тролейбус"""
        if self.passengers < self.capacity:
            self.passengers += 1

    def removePassenger(self):
        """Видалення 1 пасажира з тролейбуса"""
        if self.passengers > 0:
            self.passengers -= 1

    def __str__(self):
        """Повертає рядкове представлення об'єкта"""
        return f"Trolleybus (id = {self.id}\frouteNumber = {self.routeNumber}\fcurrentStop = {self.currentStop}\fmaxSpeed = {self.maxSpeed}\fcapacity = {self.capacity}\fpassengers = {self.passengers}"

    @staticmethod
    def getInstance():
        """Повертає єдиний екземпляр класу Trolleybus"""
        Trolleybus.instance = Trolleybus()
        return Trolleybus.instance


