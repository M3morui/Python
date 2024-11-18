# burgyonya ára 450 ft/kg
# répa ára 300 ft/kg

b = 450
r = 300
valasz = input("Milyen zöldséget szeretne? (burgonya/repa): ").lower()
mennyiseg = float(input("Mennyit szeretne vásárolni (kg): ").strip())
vegosszeg = 0
if valasz == "burgonya":
    vegosszeg = b * mennyiseg
    print(f"Választott zöldség: Burgonya, mennyiség: {mennyiseg} kg.")
elif valasz == "repa":
    vegosszeg = r* mennyiseg
    print(f"Választott zöldség: Répa, mennyiség: {mennyiseg} kg.")
else:
    print("Ismeretlen zöldségtípus")
    exit()

print(f"Fizetendő végösszeg: {vegosszeg} Ft")