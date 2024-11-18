k = 1200
m = 1500

valasz = input("Milyen eledelt szeretnél? (kutyaeledel/macskaeledel): ").lower()
mennyiseg = float(input("Mennyit szeretnél (kg): ").strip())

vegosszeg = 0
if valasz == "kutyaeledel":
    vegosszeg = k * mennyiseg
    print(f"Választott eledel: Kutyaeledel mennyiség: {mennyiseg} kg.")
elif valasz == "macskaeledel":
    vegosszeg = m * mennyiseg
    print(f"Választott eledel: Macskaeledel, mennyiség: {mennyiseg} kg.")
else:
    print("Ismeretlen eledeltípus")
    exit()

print(f"Fizetendő végösszeg: {vegosszeg} Ft")