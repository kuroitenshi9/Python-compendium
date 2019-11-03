'''
Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
(N podane przez użytkownika, ale nie większe niż 8).
'''

number = int(input("Choose number in range between 1 and 8: "))
wynik = 1

if number <= 8:
    print(f"{number}!=")
    for step in range(1, number+1):
        wynik = wynik * step
        if step < number:
            print(step, end= " * ")
        else:
            print(step, "=", wynik)
    print(f"Silnia z {number}! wynosi {wynik}")
else:
    print("Your number is too high!")