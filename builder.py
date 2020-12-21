class Vehicle:
    def __init__(self, wheels, doors, seats):
        self.wheels = wheels
        self.doors = doors
        self.seats = seats

    def __str__(self):
        return "Wheels=" + str(self.wheels) +", Doors=" + str(self.doors) + ", Seats=" + str(self.seats)

class Factory:
    def buildCar(self):
        return Vehicle(4, 5, 5)

    def buildMotocycle(self):
        return Vehicle(2, 0, 2)

if __name__ == "__main__":
    factory = Factory()

    car1 = factory.buildCar()
    car2 = factory.buildCar()
    motorcycle = factory.buildMotocycle()

    print(car1)
    print(car2)
    print(car1 == car2)
    print(motorcycle)