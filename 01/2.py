# -*- coding: utf8 -*-

"""
kalkulator BMR - Basal metabolic rate
- na podstawie wzoru BMR dostępnego np. na wikipedii w konsoli oblicz swoje BMR
"""

"""
BMR = (10 * masa ciała + 6.25 x wzrost w cm - 5 x wiek + S) * rodzaj aktywnosci

współczynnik S dla kobiet -161, dla mężczyzn + 5

rodzaj aktywności:
Praca siedząca, brak dodatkowej aktywności fizycznej	1,2
Praca niefizyczna, mało aktywny tryb życia	1,4
Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu	1,6
Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu	1,8
Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu	2,0

"""

masa = 59
wzrost = 170
wiek = 25
S = -161
aktywnosc = 1.4
BMR = (10 * masa + 6.25 * wzrost - 5 * wiek + S) * aktywnosc

print("Moje dzienne zapotrzebowanie kaloryczne wynosi",BMR, "kcal")
