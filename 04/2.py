# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki,
# które są na pozycjach parzystych. Wykonaj na dwa sposoby -
# za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’

text = input("Please give me random letter sequence: ")

for i in range(1, len(text), 2):
    print(text[i], end="")

print()

print(text[1:len(text):2])

