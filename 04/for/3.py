"""
Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
"""

sumix = 0
for num in range(1, 11):
    print(sumix)
    sumix = sumix + num
