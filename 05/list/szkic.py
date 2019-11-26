'''

▹ Policz elementy na liście, dopóki element nie będzie krotką.
numbers = [1, 2, 3, (10, 20), 4, 5]

'''
numbers = [1, 2, 3, (10, 20), 4, 5]
counter = 0
for n in numbers:
    if isinstance(n, tuple):
        break
    counter += 1
print('Wynik:', counter)

list2D = [
[0.0, 0.1, 0.2],
[1.0, 1.1, 1.2],
[2.0, 2.1, 2.2]
]