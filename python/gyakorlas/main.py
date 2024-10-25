import random
import string

# 1 feladat
# sorsolás

# nevek = ["Anna", "Béla", "Cecil", "Dávid", "Emma"]
# nev = random.choice(nevek)
# print(f"A választott név: {nev}")
# print(f"A választott nevek: {random.sample(nevek,2)}")

# 2 feladat
# mondat összerakás szavakból
# alany = ['A macska', 'A kutya', 'A kisfiú', 'A tanár']
# ige = ['fut', 'ugrik', 'alszik', 'játszik']
# targy = ['a labdával', 'a fűben', 'a házban', 'a barátokkal']
# print(f"{random.choice(alany)} {random.choice(ige)} {random.choice(targy)}.")

# 3 feladat
# jelszó generálás
karakterek = string.ascii_letters + string.digits
jelszo = "".join(random.choice(karakterek) for i in range(8))
print(jelszo)

with open("password.txt", "a") as file:
    file.write(f"{jelszo}; ")

# 4 feladat
# kő papir olló

# lista = ['kő', 'papír', 'olló']
# gep = random.choice(lista)
# user = input("Válaszz egyet(kő, papír, olló): ")

# if user == gep:
#     print("Döntetlen.")
# if user == "kő" and gep == "olló" or user == "olló" and gep == "papír" or user == "papír" and gep == "kő":
#     print("Győztél!")
# else:
#     print("Vesztettél!")

# print(f"A gép választotta: {gep}, választásod: {user}")

# 5 feladat
# bekér 1 és 200 között 15db számot
# hozzá kell adni a listához ha páros
# addig kell míg nincs meg 15db
# írd ki a lista hosszát, leellenőrizni hogy meg van-e 15
# írd ki a számokat pontos vesszővel elválasztva

# szamok = []
# while len(szamok) != 15:
#     #szam = int(input("Adj meg egy számot 1 és 200 között: "))
#     szam = random.randint(1,200)
#     if szam % 2 == 0:
#         szamok.append(szam)
# print(f"A kettes számok listájának hossza: {len(szamok)}")

# with open("numbers.txt", "w") as file:
#     file.write('; '.join(map(str,szamok)))

with open("movies.txt", "r") as file:
    lines = file.readlines()

    for i in lines:
        i = i.strip()
        szoveg = i.split()
        print(",".join(szoveg))