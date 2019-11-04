'''
 Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
 (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
 Następnie powitaj każdą osobę na liście.
'''

x = input("Podaj różne imiona po przecinku: ")
array = x.split(", ")
print(array)

for name in range(len(array)):
    print("Hello", array[name])