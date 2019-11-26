import sys

def hello_error():
    print('Początek programu')
    raise ZeroDivisionError ('To jest 0 wyjątek')
    print('Koniec programu')

try:
    hello_error()
except ZeroDivisionError as ex:
    print("Oh nie błąd", ex)

    print(sys.exc_info())

except:
    print("Inny błąd")
