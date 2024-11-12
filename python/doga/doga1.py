print("1.feladat")
a = int(input("Adj meg egy számot: "))
print(f"A szám: {a}, a szám kétszerese: {a*2}")

print("2.feladat")
b = float(input("Adj meg egy tizedes számot: "))
print(f"A szám: {b}, a szám fele: {b/2}")

print("3.feladat")
c = input("Adj meg egy mondatot: ").upper()
print(f"A mondat nagybetűsen: {c}")

print("4.feladat")
d = int(input("Adj meg egy számot: "))
if d % 2 == 0:
    print("A szám páros")
else:
    print("A szám páratlan")

import datetime as dt
print("5.feladat")
ma = dt.datetime.now()
print(ma)

print("6.feladat")
e = int(input("Adj meg egy számot: "))
f = int(input("Adj meg még egy számot: "))
print(f"A két szám: {e} és {f}, a szám összege: {e+f}, a szám külömbsége: {e-f}")

print("7.feladat")
g = float(input("Adj meg egy számot: "))
h = float(input("Adj meg még egy számot: "))
print(f"A két szám: {g} és {h}, a szám szorzata: {g*h}, a szám hányadosa: {g/h}")

print("8.feladat")
i = input(("Adj meg egy karakter láncot: "))
ihossz = print(f"A karakterek hossza {len(i)}")
ikicsi = print(f"A karakterek kicsiben {i.lower()}")

print("9.feladat")
j = float(input("Adj meg egy számot: "))
k = float(input("Adj meg még egy számot: "))
l = float(input("Adj meg még egy számot: "))
print(f"A számok átlaga: {(j+k+l)/3}")

print("10.feladat")
o = float(input("Adj meg egy számot: "))
p = float(input("Adj meg még egy számot: "))
if o > p:
    print(f"A nagyobb szám a: {o}, a kisebb a: {p}")
elif o < p:
    print(f"A nagyobb szám a: {p}, a kisebb a: {o}")

print("11.feladat")
n = input("Adj meg karaktereket: ")
elso = print(f"Az első karakter az: {n[0]}")
utolso = print(f"Az utolsó karakter az: {n[-1]}")

print("12.feladat")
oszhatoharom = False
v = float(input("Adj meg egy számot: "))
if v % 3 == 0:
    print("A szám osztható hárommal")
    oszhatoharom = True
else:
    print("Nem osztható hárommal")
    oszhatoharom = False

print("13.feladat")
y = input("Adj meg egy számot: ")
osszeg = 0
for ja in y:
    osszeg += int(ja)
print(osszeg)

print("14.feladat")
lista = [1, 2, 3, 4, 5]
osszeg = 0
for ad in lista:
    osszeg = sum(lista)
print(osszeg)

print("15.feladat")
def osszeg(a, b):
    return a + b
osszead = osszeg(10, 10)
print(osszead)

print("16.feladat")
def lista(n):
    return len(n)
print(f"A lista hossza: {lista([1,2,4,5,6])}")

print("17.feladat")
def nev(vezetek, kereszt):
    return vezetek + kereszt
teljes = nev("John ", "Doe")
print(teljes)

print("18.feladat")
def parose(x):
    if x % 2 == 0:
        print("Páros")
    else:
        print("Páratlan")
paros = parose(11)
print(paros)

print("19.feladat")
def vissza (a):
    return a[::-1]
print(f"A szöveg vissza: {vissza("asdfgh")}")

print("20.feladat")
y = int(input("Adj meg egy számot: "))
osszeg = 0
for ja in range(1, y+1):
    osszeg += ja
print(osszeg)

print("21.feladat")
b = int(input("Adj meg egy számot: "))
szamok = []
for t in range(2, b):
    if t % 2 == 0:
        szamok.append(t)
print(szamok)

print("22.feladat")
szavak = ["alma", "körte"]
for szo in str(szavak):
    print(szo)