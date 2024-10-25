# szam = 1

# while szam <= 12:
#     print(szam)
#     szam += 2

# bemenet = ""
# while bemenet.lower() != "exit":
#     bemenet = input("Írj be valamit (vagy irj be: exit a kilépéshez): ")
#     print("Te ezt írtad be: ", bemenet)

#1 feladat
#addig kell a felhasználó korát bekérni ameddig nem számot ad meg

# igaze = False

# while not igaze:
#     kor = input("Add meg a korod: ")
#     if kor.isdigit(): #isdigit = szám e amit beírtunk
#         kor = int(kor)
#         print(f"A te korod: {kor}")
#         igaze = True

# 2 feladat
#kérj be számot, addig fusson amig el nem éri az osszeg a 100at
#ha teljesul lépjen ki

# osszeg = 0
# while osszeg <= 99:
#     szam = int(input("Adj meg egy számot: "))
#     osszeg += szam

# print(osszeg)

# szamlalo = 1

# while szamlalo < 300:
#     print(str(szamlalo) + " = " + chr(szamlalo))
#     szamlalo = szamlalo + 1 # szamlalo += 1


szam = False
evszamok = []
ketezeralattiak = []
while not szam:
    evszam = input("Adj meg évszamokat: ")
    if evszam.isdigit():
        evszam = int(evszam)
        evszamok.append(evszam)
        valasz = input("Szeretnél-e még évszamot hozzáadni? ").lower()
        if valasz != "i":
            szam = True
    else:
        print("Nem számot adtál meg!")

legidosebb = 0
for kor in evszamok:
    ev = 2024-kor
    if ev > legidosebb:
        legidosebb+=ev
print(f"A lista elemei: {evszamok}")
print(f"A legidősebb: {legidosebb} éves")

for number in evszamok:
    if number < 2000:
        ketezeralattiak.append(number)
ketezeralattiak.sort()
print(ketezeralattiak)
print(len(evszamok))