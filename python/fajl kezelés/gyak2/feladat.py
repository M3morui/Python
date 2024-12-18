# Adatok beolvasása és tárolása: Olvassuk be a fájl minden egyes sorát, és tároljuk el az adatokat egy listában(név, kor, város).

# Kor szerinti rendezés: Rendezzük a beolvasott adatokat életkor szerint növekvő sorrendbe.

# Szűrés: Írjunk egy programot, ami kiírja azokat a személyeket, akik 30 évnél fiatalabbak.

# Város szerinti csoportosítás: Csoportosítsuk az adatokat a városok alapján, és írjuk ki, hogy hány személy van egy-egy városban.


lista = []
with open ("adatok.txt", "r", encoding="UTF8") as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        adat = line.split(", ")

        nev = adat[0]
        kor = int(adat[1])
        varos = adat[2]
        lista.append([nev, kor, varos])

print("1.feladat")
for item in lista:
    print(f"{item[0]}, {item[1]}, {item[2]}")

print("2.feladat")
for item in lista:
    