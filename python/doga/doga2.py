print("1.feladat")
szo = input("Adj meg egy szót: ")
if "c" in szo and "s" in szo:
    print("A szóban van c és s betű is.")
elif "c" in szo:
    print("A szóban c betű van.")
elif "s" in szo:
    print("A szóban s betű van.")
else:
    print("A szóban egyik betű sem szerepel.")


print("2.feladat")
szavak = ["A", "nap", "ragyog", "az", "égen", "és", "a", "madarak", "vidáman", "csiripelnek", "a", "fákon", "amíg", "az", "emberek", "sétálnak", "a", "parkban", "és", "élvezik", "a", "szép", "időt", "tavasz", "tarka", "tulipánok", "tündökölnek"]


i = False
while not i:
    plusz = input("Adj meg egy szót! ")
    if len(plusz) > 3:
        szavak.append(plusz)
        print(f"A listához adott szó: {plusz}")
        i = True
    else:
        print("A szónak hosszabbnak kell lennie, mint 3 betű.")
        i = False

tszo = []
for szo in szavak:
    if szo.startswith("t"):
        tszo.append(szo)
print(f"A listában {len(tszo)} t-vel kezdődő szó van.")
print(";".join(tszo))


print("3.feladat")
lista = []
with open("ajandek.txt", "r", encoding="UTF8") as fajl:
    sorok = fajl.readlines()
    for sor in sorok[1:]:
        sor = sor.strip()
        sor = sor.split(";")

        nev = sor[0]
        termek = sor[1]
        ar = int(sor[2])
        szulev = int(sor[3])
        kategoria = sor[4]

        lista.append([nev, termek, ar, szulev, kategoria])

    legf = 0
    legfn = None
    osszkat = []

    for item in lista:
        print(f"{item[0]}, {item[2]}, akciós ár: {round(item[2]*0.8)}")
        if legf < item[3]:
            legf = item[3]
            legfn = item[0]
    
        if item[4] not in osszkat:
            osszkat.append(item[4])
    
    print(f"A legfiatalabb: {legfn}, {legf}")
    print(f"A kategóriák száma: {len(osszkat)}")
        
with open("szbetuvelkezd.txt", "w", encoding="UTF8") as file:
    for item in lista:
        if item[0].startswith("Sz"):
            file.write(f"\n {item[0]}")