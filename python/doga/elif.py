# 1 feladat
#bekéri a felhasználó pontszámát, és kiirja az osztályzatot
#85 és felett kitűnő
#70-84 jeles
#50-69 közepes
#35-49 elégséges
#35 alatt elégtelen

# pontszam = int(input("Add meg a pontszámodat: "))
# if pontszam >= 85:
#     print("Kitűnő")
# elif pontszam >= 70:
#     print("Jeles")
# elif pontszam >= 50:
#     print("Közepes")
# elif pontszam >= 35:
#     print("Elégséges")
# else:
#     print("Elégtelen")

# 2 feladat
#vásárlási kedvezmény
#bekéri a vásárlás összegét
#kiszámítja a végösszeget a kedvezmány alapján
#10 000 ft alatt nincs kedvezmény
#10 000 - 20 000 ft között 10%
#20 000 ft felett 20% 

# osszeg = int(input("Add meg a vásárlásod összegét: "))
# if osszeg < 10000:
#     print("Nincs kedvezmény")
# elif osszeg < 20000:
#     kedvezmeny = 0.1
# elif osszeg > 20000:
#     kedvezmeny = 0.2

# vegosszeg = osszeg-(osszeg*kedvezmeny)
# print(f"A kedvezmény összege: {round(osszeg*kedvezmeny)} FT")
# print(f"A vásárlás végösszege: {round(vegosszeg)} FT")

#  3 feladat/doga
#hány napig akar autot berelni
#kiszámitja a bérleti dijat
#1-3 napig: 5000ft/nap
#4-7 napig: 4500ft/nap
#8 nap felett: 4000ft/nap

berles = int(input("Hány napig szeretnél autót bérelni: "))
nap1 = 5000
nap4 = 4500
nap8 = 4000 
if berles >= 8:
    print(f"A {berles} napos bérlés {berles*nap8} FT lesz.")
elif berles >= 4:
    print(f"A {berles} napos bérlés {berles*nap4} FT lesz.")
elif berles >= 1:
    print(f"A {berles} napos bérlés {berles*nap1} FT lesz.")