
'''
1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
'''

print("Zadanie 1")
zmienna = "chrzaszcz"
half = len(zmienna)//2
print("Rozwiązanie: ", zmienna[(half-1):(half+2)])


'''
2. Swórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
'''
print("Zadanie 2")
s1 = "chuj"
s2 = "chujnia"
s1_half = len(s1)//2
s3 = s1[:s1_half] + s2 + s1[s1_half:]
print("Rozwiązanie: ", s3)

'''
3. Do zmiennej quote przypisz zdanie:

„Honesty is the first chapter in the book of wisdom.”, a następnie:

-Policz wszystkie znaki w napisie
-Nie modyfikując zmiennej wyświetl słowo wisdom
-Wyświetl tylko pierwszą połowę tekstu
-Wyświetl tylko kropkę
-Wyświetl od połowy tylko co trzecią literę cytatu
-Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
-Wyświetl cały cytat odwrotnie
-Zamień wisdom na słowo friendship
'''

print("Zadanie nr 3")
quote = "Honesty is the first chapter in the book of wisdom."

#1
print("Rozwiązanie: ", len(quote))

#2
lenght = len(quote)-1
wisdom = lenght-len("wisdom")
print("Rozwiązanie: ", quote[wisdom:lenght])

#3
print("Rozwiązanie: ", quote[:(len(quote)//2)])

#4
print("Rozwiązanie: ", quote[len(quote)-1])

#5
print("Rozwiązanie: ", quote[len(quote)//2::3])

#6
print("Rozwiązanie: ", quote[::2] )

#7
print("Rozwiązanie: ", quote[::-1])

#8
print("Rozwiązanie: ", quote.replace("wisdom", "friendship"))

"9. Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową. "
"Użyj funkcji format(), by wyświetlić zdanie zawierające te wartości."

a = 12283
b = "To jest tekst"
print("A is {}, B is {}".format(a, b))
print(f"A is {a}, B is {b}")
