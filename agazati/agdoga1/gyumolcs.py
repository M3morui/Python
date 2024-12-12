alma = 150
korte = 200

print("Üdvözöljük a gyümölcsboltban!")
print("Kétféle gyümölcs kapható:")
print("1. Alma - 150 Ft/db")
print("2. Körte - 200 Ft/db")
valasz = input("Kérem, válassza ki a gyümölcsöt (alma/körte): ").lower()
mennyiseg = float(input("Kérem, adja meg, hány darabot szeretne vásárolni: ").strip())
vegosszeg = 0
if valasz == "alma":
    vegosszeg = alma * mennyiseg
    print(f"A választott gyümölcs: {valasz}")
    print(f"Mennyiség: {round(mennyiseg)}")
elif valasz == "körte":
    vegosszeg = korte* mennyiseg
    print(f"A választott gyümölcs: {valasz}")
    print(f"Mennyiség: {round(mennyiseg)}")
else:
    print("Ismeretlen gyümölcs")
    exit()

print(f"Fizetendő összeg: {round(vegosszeg)} Ft")