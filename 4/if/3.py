'''
Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.
'''

print("Hey, this program allows you to check the opinion of book. All you have to do is to input 3 ratings of the same book.\nHave fun :)\n")
book = input("Choose one book you\'d like to review: ")
rate1 = int(input("Rate the book in range 1-10: "))
rate2 = int(input("Input another rate the book in range 1-10: "))
rate3 = int(input("Rate the book again in range 1-10: "))

avg = (rate1 + rate2 + rate3)/3

if avg > 7:
    print(f"The {book} is great read!")
elif avg >= 5:
    print(f"The {book} is worth reading")
else:
    print(f"I wouldn't waste my time for shit like {book}")