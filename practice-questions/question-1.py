class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.capacity = 50 