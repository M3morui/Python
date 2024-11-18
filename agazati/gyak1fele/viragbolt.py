r = 300
t = 200

valasz = input("Milyen virágot szeretnél? (rozsa/tulipan): ").lower()
mennyiseg = float(input("Mennyit szeretnél (szál)): ").strip())

vegosszeg = 0
if valasz == "rozsa":
    vegosszeg = r * mennyiseg
    print(f"Választott virág: Rózsa, mennyiség: {mennyiseg} szál.")
elif valasz == "tulipan":
    vegosszeg = t * mennyiseg
    print(f"Választott virág: Tulipán, mennyiség: {mennyiseg} szál.")
else:
    print("Ismeretlen virág")
    exit()

print(f"Fizetendő végösszeg: {vegosszeg} Ft")