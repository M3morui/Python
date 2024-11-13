nev = input("Add meg a vizsgázó nevét! ")
pontszam = int(input("Add meg a pontszámát! "))

def szamol(nev, pontszam):
    if pontszam > 48:
        return print(f"{nev} vizsgája sikeres.")
    else:
        return print(f"{nev} vizsgája sikertelen.")
    
szamol(nev, pontszam)