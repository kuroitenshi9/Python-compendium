"""
Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.
"""
print("Hey, this program allow you to check if the sum of two integers is greater than 100.\nHave fun :)\n")
nr1 = int(input("Choose one integer: "))
nr2 = int(input("Choose another integer: "))

if nr1 + nr2 > 100:
    print(f"Great! The sum of {nr1} and {nr2} is {nr1 + nr2} and is greater than 100!")
else:
    print(f"Opps! The sum of {nr1} and {nr2} is {nr1 + nr2} and isn\'t greater than 100!")