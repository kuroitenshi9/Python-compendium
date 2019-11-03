# price = 30
#
# while (price>10):
#     print(price, "$ - za drogo")
#     price = price -2
#
# print(price, "$ super promocja!")
#

#zła pętla!
# while True:
#     print("glupi warunek")

while True:
    print("glupi warunek")
    case = input("Podaj wartość. Jeśli q = koniec programu. ")
    if case == "q":
        break


for val in "string":
    if val == "i":
        break
    print(val)

print("koniec")

print("-----------------------------")

for val in "string":
    if val == "i":
        continue
    print(val)

print("koniec")

print("----------------------------")

list_subjects = []
list_grades = []

for _ in range(3):
    subject = input("Your subject:")
    list_subjects.append(subject)
    grade = int(input("Your grade:"))
    list_grades.append(grade)

print(list_subjects)
print(list_grades)

print("----------------------")
count = 0
while count < 3:
    print(list_subjects[count], ":", list_grades[count])
    count += 1
