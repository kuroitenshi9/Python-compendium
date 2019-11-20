'''
1▹ Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. 
Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki. Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta. 
Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.
'''

class Animals:
    def __init__(self):
        print("It's an animal")

class Mammals(Animals):
    def __init__(self):
        Animals.__init__(self)
        print("It's mammal")
    
    def milk(self):
        print("Baby drinks mother's breast milk")

class Cat(Mammals):
    paws = 4
    carnivorous = True

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def description(self):
        Mammals.__init__(self)
        super().milk(self)
        print("It's a cat")

    def meow(self, sound='meow'):
        print(sound * self.age)

class Dog(Mammals):
    paws = 4
    carnivorous = True

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def description(self):
        Mammals.__init__(self)
        Mammals.milk(self)
        print("It's a dog")

    def woof(self, sound='woof'):
        print(sound * self.age)

class Human(Mammals):
    legs = 2
    vegan = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        Mammals.__init__(self)
        Mammals.milk(self)
        print("It's a human")

h = Human("Andrew", 72)
c = Cat("Pussy", 12, "Siamese")
d = Dog("Dyzio", 5, "Poodle")
m = Mammals()
a = Animals()

print('*' *20)

print(d.description())

print('*' *20)
print(h.description())


print('*' *20)
print(a)
print('*' *20)
print(m)

