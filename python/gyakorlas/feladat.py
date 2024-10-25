#feladat1
# szam = 1
# while szam < 11:
#     print(szam)
#     szam += 1

#feladat2
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

#feladat3
# szam = int(input("Kérek egy számot: "))
# osszeg = 0
# for i in range(1, szam +1):
#     osszeg += i
# print("Összege: ", osszeg)

#feladat4
# szam = int(input("Kérek egy számot: "))
# for i in range(1, 11):
#     print(szam * i)

#feladat5
# lista = [12, 75, 150, 180, 145, 525, 50]
# for i in lista:
#     if i > 500:
#         break
#     if i > 150:
#         continue
#     if i % 5 == 0:
#         print(i)

#feladat6
# szam = int(input("Kérek egy számot: "))
# szamjegyekSzama = len(str(szam))
# print(szamjegyekSzama, "db")

#feladat8
# lista = [10, 20, 30, 40, 50]
# lista = reversed(lista)
# for i in lista:
#     print(i)

#feladat9
# szamvissza = int(input("Addj egy szamot: "))
# for i in range(-(szamvissza), 0):
#     print(i)

#feladat10
for i in range(0,5):
    print(i)
else:
    print("Done!")