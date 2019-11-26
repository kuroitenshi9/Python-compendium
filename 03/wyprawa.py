#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
# Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

print("Hej! Dzieki tej funkcji dowiesz sie jaki bedzie koszt Twojej wyprawy :)")
spalanie = float(input("Ile spala Twoj samochod na 100 m? Podaj wartosc w litrach. "))
dystans = float(input("Ile wynosi dystans, który przebędziesz? Podaj wartość w metrach "))
benzyna = float(input("Jaka jest obecna cena benzyny? "))
koszt = spalanie*dystans/100*benzyna
print(koszt)
