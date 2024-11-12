try:


    fajl = open("people.csv")

    print(fajl,name)

except Exception:
    print("Nincs meg apeople.csv fájl!")
    print(f"Python szerinti hiba üzenet:{error}")
    