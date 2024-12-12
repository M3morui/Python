koridok = []

with open("autoverseny.txt", "r", encoding="UTF8") as file:
    elso = file.readlines()
    for sor in file:
        sor = sor.strip()
        adat = sor.split(";")
        koridok.append(sor)

print(f"3. feladat. {len(koridok)}")

keresett_nev = "Fürge Ferenc"
keresett_palya = "Gran Prix Circuit"
keresett_kor = "3"

for korido in koridok:
    csapat, nev, eletkor, palya, ido, kor = korido[0], korido[1], korido[2], korido[3], korido[4], korido[5]
    if nev == keresett_nev and palya == keresett_palya and kor == keresett_kor:
        ido_mpben = ido.split(";")
        ido_mpben = int(ido_mpben[0]) * 3600 + int(ido_mpben[1]) * 60 + int(ido_mpben[2])
        print(f"\n4. feladat: {ido_mpben} masodperc")

print("5. feladat")
keresett_nev = "Fürge Ferenc"
print(keresett_nev)

leggyorsabb_kor = None
for korido in koridok:
    csapat, nev, eletkor, palya, ido, kor = korido[0], korido[1], korido[2], korido[3], korido[4], korido[5]
    if nev == keresett_nev:
        ido_mpben = ido.split(";")
        ido_mpben = int(ido_mpben[0]) * 3600 + int(ido_mpben[1]) * 60 + int(ido_mpben[2])
        if leggyorsabb_kor == None:
            leggyorsabb_kor = ido_mpben
            szoveg = f"{palya}, {ido}"

        if leggyorsabb_kor > ido_mpben:
            leggyorsabb_kor = ido_mpben
            szoveg = f"{palya}, {ido}"

if leggyorsabb_kor:
    print(f"\n6.feladat: {szoveg}")
else:
    print("\n6. feladat: Nincs ilyen versenyző az állományban")