'''
def add(a: int, b: int)->int:
    return a+b

print(add(1, 2))
print(add(1.1, 2.2))
print(add("Test", "String"))

class Integer:
    pass

i1 = Integer(10)
i2 = Integer(20)

print(add(i1, i2))
'''

## Polymorphism #########

class Animal:
    def speak(self):
        print("Genereic")

class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

class Cow:
    def speak(self):
        print("Moo")


def Communicate(an: Animal):
    an.speak()

d = Dog()
# d.speak()

c = Cat()
# c.speak()

cw = Cow()


Communicate(d)
Communicate(c)
Communicate(cw)