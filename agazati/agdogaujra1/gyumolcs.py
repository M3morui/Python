print("Üdvözöljük a gyümölcsboltban!")
print("Kétféle gyümölcs kapható:")
print("1. Alma - 150 Ft/db")
print("2. Körte - 200 Ft/db")

gyumolcs = input("Kérem, válassza ki a gyümölcsöt (alma/körte): ")
db = int(input("Kérem, adja meg, hány darabot szeretne vásárolni: "))
if gyumolcs == "alma":
    ar = db*150

elif gyumolcs == "körte":
    ar = db*200
    
print(f"A választott gyümölcs: {gyumolcs}")
print(f"Mennyiség: {db} darab")
print(f"Fizetendő összeg: {ar} Ft")