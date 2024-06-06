'''
class MyType:
   def __init__(self, value) -> None:
        self.val = value 

obj1 = MyType()
obj2 = MyType()
'''


class Car:
    def __init__(self, make, model, year, color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def start(self):
        print(f"{self.year} {self.make} {self.model} is starting...")

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) in '{self.color}' color"


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

