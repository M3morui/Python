# olvassuk be a szamok.txt fájlból az adatokat. majd mentsük el a fájlba de már növekvő sorrendben.
szamok = []
with open("random_szamok.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        i = i.strip()
        szam = i.split(",")
        szamok.extend(szam)
    szamok = [int(num) for num in szamok]
    szamok.sort()
    with open("rendezett_szamok.txt", "w") as fajl:
        fajl.write(", ".join(map(str, szamok)))