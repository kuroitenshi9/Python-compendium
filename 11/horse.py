class Horse:
    def poop(self):
        print("Poop, Poop")
    def fly(self):
        print("Horse'can't fly")

class Unicorn:
    def poop(self):
        print("Rainboooow")

    def fly(self):
        print("Unicorn can fly with magical power")

def family_test(animal):
    animal.poop()

arrow = Horse()
cute = Unicorn()

family_test(arrow)