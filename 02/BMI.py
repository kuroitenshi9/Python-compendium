"""
Zapisz kalkulator BMI, który wcześniej był w konsoli do pliku,
tak aby pytał użytkownika o potrzebne do obliczeń dane.
"""

# -*- coding: utf-8 -*-
waga=float(input("Hej, ile wazysz w kg?"))
wzrost=float(input("Jaki masz wzrost w metrach?"))
print("Twoje BMI to", waga/(wzrost ** 2))
             
