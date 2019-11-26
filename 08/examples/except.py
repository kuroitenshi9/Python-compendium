
# waga = float(input("podaj swoją wagę: "))
# height = float(input("podaj swój wzrost: "))
# bmi = "nie zdefinowano"

# try:
#     bmi = waga/height ** 2
# except ArithmeticError as e:
#     print("Wzrost nie może być zerem")

# print("Twoje BMI:",bmi)


# try:
#     x = float(input("Podaj liczbę:"))
#     result = 4/x
# except ValueError as e:
#     print(e)
# except (TypeError, ZeroDivisionError) as e:
#     print(e)
# except Exception:
#     #handle all ther exceptions
#     print("Nie mam pojęcia jakim jestem błędem")

#exception pozwala na wysiwetlenie z jakim bledem mamy do czynienia 
try:
    x = float(input("Podaj liczbę:"))
    result = 4/x
except Exception as e:
    # print("Ex:", e)
    pass