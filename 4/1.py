'''
Poproś użytkownika o podanie liczby.
Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat
 “Twoja liczba jest podzielna przez 3”.
'''

x = float(input("Insert number: "))

if x%3 == 0:
    print("Your number is divisible by 3")
else:
    print("Your number is not divisible by 3")