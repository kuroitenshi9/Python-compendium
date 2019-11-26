'''
W podanym przez użytkownika ciągu wejściowym
policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.
'''

some_seq = input("Give me random sequence: ")
digits = 0
upperletters = 0
lowerletters = 0
special = 0

for char in some_seq:
    if char.isdigit():
        digits = digits + 1
    if char.isupper():
        upperletters = upperletters + 1
    if char.islower():
        lowerletters = lowerletters + 1
    if not char.isalnum():
        special = special + 1

print("The number of numbers in your string is:", digits)
print("The number of upper letters in your string is", upperletters)
print("The number of lower letters in your string is", lowerletters)
print("The number of special characters", special)


