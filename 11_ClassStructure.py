'''
class MyType:
   def __init__(self, value) -> None:
        self.val = value 

obj1 = MyType()
obj2 = MyType()
'''
from random import randint


class Car:
    # Class variable
    total_cars = 0
    country = "India"


    def __init__(self, make, model, year, color) -> None:
        self.make = make    # Read
        self.model = model  # Read
        self.year = year    # Read
        self.color = color  # Read/Write
        self.serial = self.getSerialNo()
        Car.total_cars += 1

    @property
    def Make(self):
        return self.make

    @property
    def Model(self):
        return self.model
    
    @property
    def Year(self):
        return self.year
    
    @property
    def Color(self):
        return self.color

    @Color.setter
    def Color(self, value):
        self.color = value


    def start(self):
        print(f"{self.year} {self.make} {self.model} is starting...")

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) in '{self.color}' color [{self.serial}]"

    @classmethod
    def getTotalCars(cls):
        return f"{Car.total_cars} in {cls.country}"

    @staticmethod
    def getSerialNo():
        return randint(1, 100)



class GearedCar(Car):
    country = "Hyderabad"

    def __init__(self, make, model, year, color, gear_count) -> None:
        super().__init__(make, model, year, color)
        self.gear_count = gear_count




###################################################################################
'''
car1 = Car("Toyota", "Camry", 2024, "Blue")
car2 = Car("Honda", "Accord", 2023, "Red")

car1.start()
car2.start()

# print(car1.GetDetails())
# print(car2.GetDetails())

print("\n", "-"*10)
print(car1)
print(str(car1))
print(car1.__str__())       # Stringified object
print(car1.__repr__())      # Object representation
print("-"*10, "\n")

print(car1, car2, sep="\n")

print(car1.getTotalCars())
print(car1.__class__.getTotalCars())
print(Car.getTotalCars())

gc1 = GearedCar("Honda", "Accord", 2023, "Red", 5)
print(gc1.getTotalCars())
print(gc1.__class__.getTotalCars())
print(GearedCar.getTotalCars())

print("\n", "-" * 10, "\n")
print(car1)
print(car2)
print(gc1)
'''


car1 = Car("Toyota", "Camry", 2024, "Blue")
car2 = Car("Honda", "Accord", 2023, "Red")

print(car1.Color)
car1.Color = "Black"
print(car1)

# car1.Make = "Maruti"
color = car1.Make
print(car1.Make)