mennyiseg = input("Milyen mértékegységről szeretne átváltani? (liter/dl): ")
szam = int(input("Adja meg az átváltandó mennyiséget: "))

if mennyiseg == "dl":
    print(f"{szam} deciliter = {round(szam*0.1)} liter")
if mennyiseg == "liter":
    print(f"{szam} liter = {round(szam*10)} deciliter")