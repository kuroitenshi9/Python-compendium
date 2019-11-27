'''
Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch znaków 
i zwracający ten sam tekst zmieniony na wielkie litery.
Utwórz funkcję zwracającą tekst
Utwórz dekorator przyjujący tę funkcję
Wywołaj funkcję, by sprawdzić, że decorator działa
'''

import random
list  = ["there was sunshine when she's gone", "highway to hell", "she is standing and so on", "show must go on", "can't take my eyes of you"]


def uppercase_decorator(textf):
    def sometext():
        text = textf()
        text = text.upper()
        return text
    return sometext

@uppercase_decorator
def hi():
    x = random.choice(list)
    return x

print(hi())
