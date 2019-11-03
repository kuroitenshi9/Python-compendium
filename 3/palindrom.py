'''
Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
'''

zdanie = input("Wpowadź dowolne zdanie a ja sprawdzę czy to palindrom: ")
zdanie = zdanie.upper().replace(" ", "")
print(zdanie == zdanie[::-1])