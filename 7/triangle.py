#trojkat
def triangle_field(base, height):
   pole_trojkata = base*height/2
   return pole_trojkata

print("pole trojkata")
a= 5
h= 10

print(triangle_field(a, h))

#kolo
def circle_field(r):
   pole_kola = 3.14 * r**2
   return pole_kola

print("pole kola")

r = 5
print(circle_field(r))

#kwadrat
def square_field(a):
   pole_kwadratu = a**2
   return pole_kwadratu

print("pole kwadratu")

a = 5
print(square_field(a))

#trapez
def trapeze_field(a, b, h):
   pole_trapezu =  (a + b)*h/2
   return pole_trapezu


print("pole trapezu")
a = 2
b = 3
h = 5
print(trapeze_field(a,b,h))