from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        print("Genereic")

    @abstractmethod
    def move(self):
        print("Displace")

class Dog(Animal):
    def speak(self):
        print("Woof")

    def move(self):
        print("Run")

class Cat(Animal):
    def speak(self):
        print("Meow")

    def move(self):
        print("Run")

class Cow(Animal):
    def speak(self):
        print("Moo")

    def move(self):
        print("Saunter")

def Communicate(an: Animal):
    an.speak()

# a = Animal()
d = Dog()
c = Cat()
cw = Cow()


# Communicate(a)
Communicate(d)
Communicate(c)
Communicate(cw)