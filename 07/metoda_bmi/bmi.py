# -*- coding: utf-8 -*-
waga = float(input("Hej, ile wazysz w kg?"))
wzrost = float(input("Jaki masz wzrost w metrach?"))

BMI = waga/(wzrost ** 2)


def bmi_status(BMI):
    if BMI < 10:
        return "powazna niedowaga"
    elif BMI < 18.5:
        return "niedowaga"
    elif BMI < 25:
        return "normalna waga"
    elif BMI < 30:
        return "nadwaga"
    else:
        return "otylosc"

print("Twoje BMI to", BMI, bmi_status(BMI))
