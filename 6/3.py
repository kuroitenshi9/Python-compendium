'''
3▹ Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystkich elementów na liście.
'''
# def avg():
#     numbers = input("Insert numbers and divide them by comma: ")
#     numbers = numbers.split(", ")
#     for n in numbers:
#         n = float(n)

truth = "beauty"
index = 0
letters = []
while index < len(truth):
    letters.append(truth[index])
    index += 2

letters = '-'.join(letters)
print(letters)