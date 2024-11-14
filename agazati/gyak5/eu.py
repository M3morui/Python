lista = []
from datetime import datetime

with open ("Eucsatlakozas.txt", "r", encoding="UTF8") as fajl:
    sorok = fajl.readlines()
    for sor in sorok:
        sor = sor.strip()
        sor = sor.split(";")

        orszag = sor[0]
        datum = datetime.strptime(sor[1], "%Y.%m.%d")

        lista.append([orszag, datum])


legutoljara = 0
legutoljaranev = None
csatlakozok2007 = 0
evek = []

for item in lista:
    # print(f"{item[0]}, {item[1].year}")
    if item[1].year == 2007:
        csatlakozok2007 += 1
    if item[0] == "Magyarország":
        print(f"{item[0]} csatlakozásának dátuma: {item[1].month}")
    
    if item[0] == "Magyarország" and item[1].month == 5:
            print(f"6.feladat: Májusban volt a csatlakozás!")

    if item[1].year > legutoljara:
        legutoljara = item[1].year
        legutoljaranev = item[0]


    if item[1].year not in evek:
        evek.append(item[1].year)

print(evek)
print(f"7.feladat: Legutoljára csatlakozott ország: {legutoljaranev}")
print(f"3.feladat: EU tagállamok száma: {len(lista)} db")
print(f"4.feladat: 2007-ben {csatlakozok2007} ország csatlakozott.")

