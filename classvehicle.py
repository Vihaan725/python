class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
speedmileage = vehicle(130, 35)
print("The car's max speed(miles) is: ", speedmileage.max_speed)
print("The cars average mileage(miles) is: ", speedmileage.mileage)