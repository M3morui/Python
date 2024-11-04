from datetime import datetime
lista = []
yettel = []
telekom = []
vodafon = []
legfiatal = datetime.min
legfiatalnev = None
with open("diakok.txt", "r", encoding="UTF8") as file:
    lines = file.readlines()

    for line in lines[1:]: #elso sort kihagyjuk
        line = line.strip()
        adat = line.split(";")

        nev = adat[0]
        atlag = float(adat[1])
        telefon = adat[2]
        szuletes = datetime.strptime(adat[3], "%Y-%m-%d")
        lista.append([nev, atlag, telefon, szuletes])

for item in lista:
    # print(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}")
    if item[3] > legfiatal:
        legfiatal = item[3]
        legfiatalnev = item[0]
    if item[2].startswith("+3620"):
        yettel.append(item[0])
    elif item[2].startswith("+3630"):
        telekom.append(item[0])
    elif item[2].startswith("+3670"):
        vodafon.append(item[0])

print(f"A legfiatalabb: {legfiatalnev}, {legfiatal}")


with open("szolgaltato.txt", "w", encoding="UTF8") as fajl:
    fajl.write("20-as telefonszámok:")
    for y in yettel:
        for i in lista:
            if y == i[0]:            
                fajl.write(f"\n{y}, {i[2]}")

    fajl.write("\n")
    fajl.write("\n30-as telefonszámok:")
    for t in telekom:
        for i in lista:
            if t == i[0]:            
                fajl.write(f"\n{t}, {i[2]}")

    fajl.write("\n")
    fajl.write("\n70-as telefonszámok:")
    for v in vodafon:
        for i in lista:
            if v == i[0]:            
                fajl.write(f"\n{v}, {i[2]}")