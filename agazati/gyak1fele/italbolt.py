a = 150
gy = 450

valasz = input("Milyen italt szeretnél? (viz/gyumolcsle): ").lower()
mennyiseg = float(input("Mennyit szeretnél (l): ").strip())

vegosszeg = 0
if valasz == "viz":
    vegosszeg = a * mennyiseg
    print(f"Választott ital: Ásványvíz, mennyiség: {mennyiseg} l.")
elif valasz == "gyumolcsle":
    vegosszeg = gy * mennyiseg
    print(f"Választott ital: Gyümölcslé, mennyiség: {mennyiseg} l.")
else:
    print("Ismeretlen italtípus")
    exit()

print(f"Fizetendő végösszeg: {vegosszeg} Ft")