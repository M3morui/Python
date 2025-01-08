mertekegyseg = input("Milyen mértékegységről szeretne átváltani? (liter/dl): ")
mennyiseg = int(input("Adja meg az átváltandó mennyiséget: "))

if mertekegyseg == "liter":
    eredmeny = mennyiseg*10
    print(f"Az eredmeny: {round(eredmeny)} dl.")


elif mertekegyseg == "dl":
    eredmeny = mennyiseg / 10
    print(f"Az eredmeny: {round(eredmeny)} liter.")