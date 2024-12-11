from datetime import datetime

szemelyek = []

with open("balkezesek.txt", "r", encoding="UTF8") as fajl:
    sorok = fajl.readlines()

    elso_sor =  sorok[0].strip()
    print(elso_sor)

    for sor in sorok[1:]:
        sor = sor.strip()
        sor = sor.split(";")

        nev = sor[0]
        elso = (datetime.strptime(sor[1], "%Y-%m-%d"))
        utolso = (datetime.strptime(sor[2], "%Y-%m-%d"))
        suly = int(sor[3])
        magassag = int(sor[4])

        szemelyek.append([nev, elso, utolso, suly, magassag])

print(f"3.feladat {len(szemelyek)}")
print(f"4.feladat: ")
ev = 0
sz = ""
magassag = None
for szemely in szemelyek:
#     print(f"{szemely[0]}, {szemely[1]}, {szemely[2]}, {szemely[3]},{szemely[4]}")
    if szemely[1].year == 1999 and szemely[1].month == 10 or szemely[2].year == 1999 and szemely[2].month == 10:
        ev = szemely[1]
        sz = szemely[0]
        magassag = szemely[4]*2.54
        print(f"{sz}, {round(magassag,1)} cm")

print(f"5.feladat: ")
while True:
    evszam = int(input("Kérek egy 1990 és 1999 közötti évszamot: "))
    if evszam >= 1990 and evszam <= 1999:
        print(f"A meadott zsám: {evszam}")
        break
    else:
        print(f"Hibás adat! Kérek egy 1990 és 1999 közötti évszamot!: ")


sulyok = []
for suly in szemelyek:
    if suly[1].year == evszam or suly[2].year == evszam:
        sulyok.append(suly[3])
print(f"6.feladat: {round(sum(sulyok)/len(sulyok),2)} font")