class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def showcarmodel(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        self.fuel_type = fuel_type
        super().__init__(brand, speed)

C = Car("Tesla", "Model 3", "Unleaded")

print("Is car a subclass of Vehicle", issubclass(Car, Vehicle))