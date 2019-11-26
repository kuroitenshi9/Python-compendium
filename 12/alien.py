import random

class Player:
    def blast(self, enemy):
        print(f'{player_name} strzela we wroga. \n')
        strike = random.randrange(0, 10)
        if strike > 3:
            enemy.die()
        else:
            enemy.win()

class Alien:
    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')
    def win(self):
        print(f'{player_name} strzela w stronę Obcego, ale ten zwinnie omija pocisk. \n',
            f'Obcy dopada {player_name} i pożera w całości. \n',
            'Oblizuje się ze smakiem po czym ucina drzemkę') 

if __name__ == '__main__':
    print('************ Welcome to the game Alien Slayer ************\n')
    player_name = input("Choose name for the player: ")
    hero = Player()
    invader = Alien()

    hero.blast(invader)
    input('\n\nPress Enter to quit game.')
    