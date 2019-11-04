'''
 Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
'''

numbers = input("Podaj 10 liczb po przecinku: ")
numbers = numbers.split(",")
# print(numbers)

odd_numbers = []

for n in numbers:
    n = int(n)
    if n % 2 == 1:
        odd_numbers.append(int(n))

print(odd_numbers)