"""
kalkulator zapotrzebowania kalorycznego 2
Zapisz kalkulator BMR dla kobiet, który wcześniej był w konsoli do pliku,
tak aby pytał użytkownika o potrzebne do obliczeń dane.
"""

waga=float(input("Ile wazysz?"))
wzrost=float(input("Jaki masz wzrost w cm?"))
wiek=float(input("Ile masz lat?"))
S=-161
aktyw=float(input("Jaka jest Twoja aktywnosc fizyczna? Wybierz jedna liczbe wsrod: \n Praca siedząca, brak dodatkowej aktywności fizycznej  1.2 \n Praca niefizyczna, mało aktywny tryb życia	1.4  \n Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu	1.6 \n Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu	1.8 \n Praca fizyczna ciężka, regularne ćwiczenia 7 razy w tygodniu 2.0"))
print("Twoje zapotrzebowanie kaloryczne wynosi:", (10 * waga + 6.25 * wzrost - 5 * wiek + S) * aktyw)
