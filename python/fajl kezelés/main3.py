names = []
with open("osztalyatlag.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        i = i.strip()
        nev,atl = i.split(";")
        names.append((nev,float(atl)))

negyesfelettiek = []
eredmenyek = 0
for nev, atl in names:
    eredmenyek += atl
    if atl > 4:
        negyesfelettiek.append(nev)

with open("atlag.txt", "w") as fajl:
    fajl.write(f"Az átlag: {eredmenyek/len(names)}")
    fajl.write("; ".join(map(str,negyesfelettiek)))
    