'''
Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:

Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.

Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich

Połącz dane w jeden ciąg book za pomocą spacji

Policz liczbę wszystkich znaków w napisie book
'''

title = input("Jaki jest tytuł książki?: ")
author = input("Jakie jest nazwisko autora?: ")
page = input("Ile książka ma stron?: ")

print(title.isalpha())
print(author.isalpha())
print(page.isdigit())
book = [title.title(), author.title(), page]
print(" ".join(book))