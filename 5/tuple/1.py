
'''
 Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). 
 Następnie rozpakuj tę krotkę na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia f-stringa, 
 tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”.
'''

my_pet = ("dog", "labrador", "Tysio")
(animal, type, name) = my_pet

print(f"My pet is {animal}, it's {type} breed and it's name is {name}")