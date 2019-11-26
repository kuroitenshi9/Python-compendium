'''
stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”
'''

backpack = ["shoes", "apple", "chocolate", "rope", "jacket"]
for step, name in enumerate(backpack):
    print("Packed: ", name)
print()
for step in range(len(backpack)):
    print("Packed: ", backpack[step])
