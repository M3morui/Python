print("Üdvözöljük a halboltban!")
print("Kétféle hal kapható:")
print("Lazac - 3000 Ft/kg")
print("Pisztráng - 2500 Ft/kg\n")

hal = input("Kérem, válassza ki a halat (lazac/pisztráng): ")
db = int(input("Kérem, adja meg, hány kilogrammot szeretne vásárolni:"))
if hal == "Lazac":
    mennyiseg = 3000*db
    print(f"A választott hal: {hal}")
    print(f"Mennyiség: {db} kg")
    print(f"Az összeg: {mennyiseg}")
if hal == "pisztráng":
    mennyiseg = 2500*db
    print(f"A választott hal: {hal}")
    print(f"Mennyiség: {db} kg")
    print(f"Az összeg: {mennyiseg}")