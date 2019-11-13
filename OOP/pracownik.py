'''
6▹ Utwórz klasę Pracownik.

Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.

Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia. 

Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.

Pracownik powinien mieć pole typu boolowskiego zawierające status studenta. Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.

Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.

Adam Kowalski Love Python Company

email -> smkwlsk@lovepythoncompany.com
'''

class Employee:
    company = "Pajton paradise"
    def __init__(self, position, salary, name, surname, seniority, is_student):
        self.position = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.seniority = seniority
        self.is_student = is_student

    def yearly_salary_raise(self):
        self.salary = self.salary + self.salary * (0.05 + self.seniority * 0.1)
        return self.salary

    def tax(self):
        return self.salary * 0.02

    def health_care(self):
        if self.is_student:
            proc = 0
        else:
            proc = 0.1
        return self.salary * proc

    def email(self):
        primary = self.name + "." + self.surname
        secondary = self.company.replace(" ", "").lower() + ".com"
        email = primary.lower() + "@" + secondary
        return email

p1 = Employee("programista", 5500, "Jan", "Kowal", 3, False)
print(p1.name)
print(p1.surname)
print(p1.salary)
print(p1.yearly_salary_raise())
print(p1.salary)
print(p1.email())

