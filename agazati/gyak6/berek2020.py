lista = []

with open ("berek2020.txt", "r", encoding="UTF8") as file:
    header = file.readline().strip()
    print(header)

    for line in file:
        line = line.strip()
        line= line.split(";")

        nev = line[0]
        neme = line[1]
        reszleg = line[2]
        belepes = int(line[3])
        ber = int(line[4])

        lista.append([nev, neme, reszleg, belepes, ber])

berek2020 = []
beker = input("Kérem egy részleg nevét: ")

lneve = ""
lneme = ""
lbelepes = None
lber = 0
for list in lista:
    # print(f"{list[0]}, {list[1]}, {list[2]}, {list[3]}, {list[4]}")
    berek2020.append(list[4])
    if beker in list[2]:
        if list[4] > lber:
            lber = list[4]
            lneve = list[0]
            lbelepes = list[3]
            lneme = list[1]
            print(f"\nNév: {lneve}, Neme: {lneme}, Belépés: {lbelepes}, Bér: {lber}")
    elif beker not in list[2]:
        print("A megadott részleg nem létezik.")
        break


print(f"3.feladat: Dolgozók száma: {len(lista)} fő")
print(f"4.feladat: Bérek átlaga: {round(sum(berek2020)/len(berek2020)), 1} Ft")