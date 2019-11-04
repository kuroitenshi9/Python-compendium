def predict_future():
    num = int(input("Podaj dowolną liczbę naturalną: "))
    if num < 0:
        raise ValueError("To nie jest liczba naturalna!")
    else:
        print("Za", 10 * num, "lat ludzkość będzie mogła się teleportować")

try:
    predict_future()
except TypeError as e:
    print("*")
    print(e)
except ValueError as e:
    print("~")
    print(e)