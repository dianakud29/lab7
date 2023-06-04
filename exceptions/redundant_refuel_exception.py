class RedundantRefuelException(Exception):
    def __init__(self, message="Redundant refuel attempted"):
        self.message = message
        super().__init__(self.message)

