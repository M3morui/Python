nev = input("Add meg a vizsgázó nevét! ")
pontszam = int(input("Add meg a pontszámát! "))


def szamol(pontszam):
    if pontszam > 48:
        return print(f"{nev} vizsgája sikeres.")
    if pontszam <= 48:
        return print(f"{nev} vizsgája sikertelen.")

szamol(nev, pontszam)

ures = True
while ures:
    nev = input("Add meg a vizsgázó nevét! ")
    if nev == "":
        ures = False
        break