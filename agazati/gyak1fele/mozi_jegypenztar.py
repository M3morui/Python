f = 1200
gy = 1500

valasz = input("Milyen jegyet szeretnél? (gyerek/felnott): ").lower()
mennyiseg = float(input("Mennyit szeretnél (db): ").strip())

vegosszeg = 0
if valasz == "felnott":
    vegosszeg = f * mennyiseg
    print(f"Választott jegy: Felnőtt mennyiség: {mennyiseg} db.")
elif valasz == "gyerek":
    vegosszeg = gy * mennyiseg
    print(f"Választott jegy: Gyerek, mennyiség: {mennyiseg} db.")
else:
    print("Ismeretlen jegytípus")
    exit()

print(f"Fizetendő végösszeg: {vegosszeg} Ft")