
import random

class Dog:
    tail = True

    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.pseudo = name + "-" + color
        # self.pseudo2 = pseudo2()

    def pseudo2(self):
        characters = ["destroyer", "weirdo", "player", "maneater", "vegan", "shotgun"]
        return self.name + "-" + random.choice(characters)
    
    def bark(self):
        return "wooh " * self.age

    def wag_a_tail(self):
        return "wags " * len(self.name)


obj_pimpek = Dog("Pimpek", "Collie", 5, "white" )
print(obj_pimpek.name)
print(obj_pimpek.pseudo)
print(obj_pimpek.tail)
print(Dog.tail)

print(obj_pimpek.pseudo2())
print(Dog.pseudo2(obj_pimpek))
print(obj_pimpek.bark())
print(obj_pimpek.wag_a_tail())


names = "Anna, Marta, Marek, Paweł"
print(names.split(","))
print(type(names))
print(str.split(names, ","))