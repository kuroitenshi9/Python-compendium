'''
2) Napisz prostą grę, w której użytkownik musi
zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
'''

import random

secret = random.randint(0, 20)
guess = 0

print('Let\'s play game! Try to guess my secret number in range 0-20!')
while guess != secret:
    guess = int(input('Your guess? '))
    if guess != secret:
        print(f"Oops. {guess} is not my secret number :( Try again!")

print(f"You've guessed correctly! {secret} is my secret number!")

