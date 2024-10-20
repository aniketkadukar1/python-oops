from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def run(self):
        pass

class Dog(Animal):

    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color
    
    #accessors
    def get_name(self):
        return self.__name

    #mutators
    def set_name(self, name):
        self.__name = name

    def make_sound(self):
        print("Bho wow")
    
    def run(self):
        print("Dog is walking")

class Cat(Animal):
    a = 1
    def make_sound(self):
        print("meaw")
    
    def run(self):
        print("Cat is walking")   


d = Dog("Bruno", 3, "White")
d.set_name("Neko")
print(d.get_name())


c = Cat()

d.make_sound()
d.run()

c.make_sound()
c.run()