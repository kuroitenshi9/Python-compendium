class Vertebrate:
    backbone = True
    
    def __init__(self):
        print("Szkielet wewnętrzny kręgowców...")

    def desc(self):
        return "Zewnętrzną pokrywę ciała kręgowców stanowi skóra"

class Cat(Vertebrate):
    def __init__(self, name):
        print("Kotek!")
        self.name = name

    def desc(self):
        super().desc()
        print("Koty są super")

ver = Vertebrate()
kitty = Cat("Kitty")
kitty.desc()