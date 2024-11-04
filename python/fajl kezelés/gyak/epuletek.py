lista = []
varosok = []
regiepuletnev = None
regiepuletev = float("inf")
with open("epuletek.txt", "r", encoding="UTF8") as file:
    lines = file.readlines()

    for line in lines[1:]: #elso sort kihagyjuk
        line = line.strip()
        adat = line.split(";")

        epuletnev = adat[0]
        varos = adat[1]
        orszag = adat[2]
        magassag = int(adat[3])
        emelet = int(adat[4])
        epultev = int(adat[5])
        lista.append([epuletnev, varos, orszag, magassag, emelet, epultev])

for item in lista:
    print(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]},  {item[5]}")

    # Adjátok meg hány város található a listába és ezt írjátok ki ismétlés nélkül
    if item[1] not in varosok:
        varosok.append(item[1])

    # Adjátok meg melyik a legrégebbi épület, írjátok ki a nevét és az évet.
    if item[5] < regiepuletev:
        regiepuletev = item[5]
        regiepuletnev = item[0]

print(f"{regiepuletnev}, {regiepuletev}")
print("; ".join(varosok))
print(f"A városok száma: {len(varosok)}")

