class UsefulStuff:
    def __init__(self):
        print("I'm just useful")

class Phone:
    def __init__(self):
        print("I can call")

class Watch:
    def __init__(self):
        print("I can check: what time it is")

class Smartwatch(Watch, Phone):
    def __init__(self):
        print("I'm smartwatch")
        super().__init__()


u = UsefulStuff()
w = Watch()
p = Phone()
