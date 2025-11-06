class car:
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = int(mileage)

    def __str__(self):
        return f"The {self.colour} car has {self.mileage:,} miles"

bluecar = car('blue',20_000)
redcar = car('red',30_000)

for car in (bluecar, redcar):
    print(car)