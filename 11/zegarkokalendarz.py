import datetime
class Zegarek():
    def __init__(self):
        pass

    def current_time(self):
        return datetime.datetime.now().time()

class Kalendarz():
    def __init__(self):
        pass

    def current_date(self):
        return datetime.datetime.now().date()

    def show_calendar(self):
        for i in range (1, 31):
            if i % 7 == 0:
                print(i)
            else:
                print(i, end="")

class ZagarkoKalendarz(Zegarek, Kalendarz):

    def current_date_time(self):
        print(super().current_date())
        print(super().current_time())
        print(super().show_calendar())

zk = ZagarkoKalendarz()
zk.current_date_time()

print(zk)