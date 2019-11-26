#
# text = "abdd"
# for i in text:
#     print("-" + i)
#
# '''
# for letter in text:
#     print("-" + letter)
# '''
#
# print()
#
# arr = ["aaaa", "aaab", "caaaa", "heie",]
#
# for a in arr:
#     print("Hello", a)
# print()
# for step in range(5, 100, 5):
#     print("krok: ", step)
# print()
# for step in range(5, 101, 5):
#     print("krok: ", step)
# ctr + / = komentarz

names = ["Ada", "Julia", "Ruby", "Python"]

for id in range(len(names)):
    print(id, ":", names[id])

print()

for id, name in enumerate(names):
    print(id, ":", name)


pa = ""
magic = "hokuspokus"

for num in range (2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)

print("final password: ", pa)
