# number = 5
# number = "szam"
# print(number)

# kor = int(input("Add meg a korod: "))
# print(f"A te korod: {kor} éves")

# if kor > 18:
#     print("Megnézheted ezta filmet.")
# elif kor < 18:
#     print("Nem nézheted meg.")
# else:
#     print("Egyenlő 18-al.")

szam1 = int(input("Add meg az első számot: "))
szam2 = int(input("Add meg a második számot: "))

result = szam1 + szam2
print(f"Az eredmény: {result}")

if result % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")

#12, 1, 2: Tél
#3, 4, 5: Tavasz
#6, 7, 8: Nyár
#9, 10, 11:Tél
#Be kell kérni egy számot ami az adott hónapot prezentálja.

# honap = int(input("Adj meg egy számot 1 és 12 között: "))
# if honap == 12 or honap == 1 or honap ==2:
#     print("Tél")
# elif honap == 3 or honap == 4 or honap == 5:
#     print("Tavasz")
# elif honap == 6 or honap == 7 or honap == 8:
#     print("Nyár")
# elif honap == 9 or honap == 10 or honap ==11:
#     print("Ősz")
# else:
#     print("Nem számot adtál meg.")

# Kérj be egy egész számot, és írd ki
# a kétszeresét,
# a heted részét (2 tizedes jegyre kerekítve),
# a négyzetgyökét (0.5-ödik hatvány),
# 3-mal osztva a hányados egész részét és a maradékot, és hogy
# páros vagy páratlan. (Tipp: egy szám egész, ha egyenlő az egészrészével.)
# Minta:
# Írj be egy pozitív egész számot: 15
# A szám kétszerese: 30
# A szám heted része: 2.14
# 3-mal osztva az egészrész: 5 amaradék: 0
# A szám páratlan

# bekertszam = int(input("Írj be egy pozitív egész számot: "))
# print(f"A szám kétszerese: {bekertszam * 2}")
# print(f"A szám heted része: {round(bekertszam / 7,2)}") #round kerekítés
# print(f"3-mal osztva az egészrész: {round(bekertszam / 3)} amaradék: {bekertszam % 3}")
# print("A szám páros." if bekertszam % 2 == 0 else "A szám páratlan.")

#Kérd be a felhasználó korát. És mond meg melyik évben született.
#import datetime
#kor = int(input("Add meg a korod: "))
#ev = int(input("Add meg az aktuális évet: "))
#ev = datetime.datetime.now()
#print(f"Te ebben az évben születtél: {ev.year- kor}")