# megad = False
# while not megad:
#     szemely = int(input("Hány személyre lesz a  foglalás(felnőtt): "))
#     nap = input("Hány napra foglalna szállást: ")
#     gyerek = int(input("Hány kiskorú van: "))

#     if nap.isdigit():
#         nap = int(nap)
#         if nap > 0:
#             if gyerek <= 2:
#                 osszeg = (nap * szemely *5000)-(gyerek * 700)
#                 megad = True
#             elif gyerek >= 10:
#                 osszeg = (nap * szemely *5000)-(gyerek * 1000)
#                 megad = True
#             elif gyerek == 0:
#                 osszeg = nap * szemely *5000
#                 megad = True
#         else:
#             print("0-nál kisebb számot adtál meg.")
#     else:
#         print("Nem számot adtál meg.")
# print(f"A fizetendő összeg: {osszeg}")

#kérjen be a program 3 virágot, vagy rózsa, vagy tulipán, vagy liliom
#hány szál virágot szeretne, addig kérje a program míg legalább egyet ír
#1db rózsa=500ft, 1db tulipán=400ft, 1db liliom=300ft
#irja ki a végösszeget

# szam = False
# while not szam:
#     virag = input("Milyen virágot szeretnél tulipán(T), rózsa(R), liliom(L)? ").upper()
#     db = input("Hányat szál virágot szeretnél? ")
#     if db.isdigit():
#         db = int(db)
#         if db > 0:
#             if virag == "T":
#                 osszeg = db*400
#                 szam = True
#             elif virag == "R":
#                 osszeg = db*500
#                 szam = True
#             elif virag == "L":
#                 osszeg = db*300
#                 szam = True
#     else:
#         print("Nem számot adtál meg.")

# print(f"A virágok ára: {osszeg} Ft")


# ujabbosszeg = False
# shop = []
# while not ujabbosszeg:
#     termek = int(input("Add meg a termék összegét: "))
#     if termek > 0:
#         shop.append(termek)
#         valasz = input("Szeretnéd-e a terméket hozzáadni a listához? ").lower()
#         if valasz != "i":
#             ujabbosszeg = True

# tizezeralatt = []
# for i in shop:
#     if sum(tizezeralatt) + i < 10000:
#         tizezeralatt.append(i)
# print(f"A tizezeralatt lista osszege: {sum(tizezeralatt)}")
# print(f"A megvásárolható termekek: {len(tizezeralatt)} db")

# print(f"Legnagyobb összeg: {max(shop)} Ft")
# print(f"A legkisebb összeg: {min(shop)} Ft")
# print(f"A lista elemeinek száma: {len(shop)} db")
# print(f"A teljes lista tartalmának az összege: {sum(shop)} Ft")

#bevásárlások összegét kell eltárolni egy listában
#irasd ki a konzolra a termékek összegét, megyik volt a legdrágább, legolcsóbb
#hány terméket tudnál 25 000ft-ból megvenni

# ujtermek = False
# ar = []
# while not ujtermek:
#     vasarlas = int(input("Add meg a termék összegét: "))
#     if vasarlas > 0:
#         ar.append(vasarlas)
#         meg = input("Van-e még új összeg? ")
#         if meg != "i":
#             ujtermek = True
# huszonotkalatt = []
# for i in ar:
#     if sum(huszonotkalatt) + i < 25000:
#         huszonotkalatt.append(i)
# print(f"A termékek összege: {sum(ar)} Ft")
# print(f"A legnagyobb ár: {max(ar)} Ft")
# print(f"A legkisebb ár: {min(ar)} Ft")
# print(f"A 25k alatti lista összege: {sum(huszonotkalatt)}")
# print(f"Az eredeti lista termékeinek száma: {len(ar)} db")
# print(f"A megvásárolható termékek száma: {len(huszonotkalatt)} db")

