'''
Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. 
Napisz funkcję, która przyjmie wartości i wyświetli średnią. 
Program powinen być odporny na błędy użytkownika. Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
'''

numbers = input("Podaj ciąg liczb rozdzielonych przecinkiem: ")
numbers = numbers.split(",")
print(numbers)

list_exc =[]
for index, elem in enumerate(numbers):
    try:
    # print(index, ":", elem)
        numbers[index] = float(elem)
    except ValueError as exc:
        list_exc.append(exc)
        numbers[index] = '-'

print(numbers)

while '-' in numbers:
    numbers.remove('-')
print(numbers)

avg = sum(numbers)/len(numbers)
print(avg)
print(list_exc)

with open("errors.txt", "w") as f:
    f.write("Ha mamy błędy\n")
    for i in list_exc:
        f.write(str(i) + "\n")

# def average:
#     some_numbers = input(float("Podaj kilka liczb po przecinku: "))
#     some_numbers = numbers.split(",")
#         for numbers in some_numbers:
#             number = float(number)
        
    #         try:
    #     result = 10 / elem
    # except ZeroDivisionError as e:
    #     result = "Wyjątek 1:" + str(e)
    # except TypeError as e:
    #     result = "Wyjątek 2:" + str(e)
    
    # print(result)
    