'''
3. Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.
'''
numbers = input("Please input some numbers and divide them by comma: ")
numbers = numbers.split(", ")

if numbers[0] == numbers[-1]:
    print("Your first and last number is the same!")
else:
    print("Your first and last number is different!")

