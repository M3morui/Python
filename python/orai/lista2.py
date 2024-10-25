# jegyek = [2,3,4,5,2,5,2,5,3,1,4,4,5,3,2,5,5]
# for i in range(1,6):
#     db = 0
#     for szam in jegyek:
#         if i == szam:
#             db+=1
#     print(f"Az érdemjegyből: {i}-ből {db} db van.")

# lista = ["alma", "eper", "körte", "cseresznye", "körte", "körte", "eper", "eper", "eper"]
# rendezett_lista = []
# for i in range(len(lista)):
#     db=0
#     if lista[i] not in rendezett_lista:
#         for list in lista:
#             if lista[i] == list:
#                 db+=1
#         print(f"Az {lista[i]} szóból, {db} van.")
#         rendezett_lista.append(lista[i])

# minta:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

# for i in range(3):
#     for j in range(1,16):
#         if j == 15:
#             print(j)
#         else:
#             print(j, end=", ")

# minta
# 1
# 1, 2
# 1, 2, 3
# 1, 2, 3, 4
# ....

# piramis = int(input("Adj meg egy számot: ")) 
# print("Piramis formában egészen a magadott számig")
# for i in range(piramis):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()
# verzio 2.0
# for i in range(1, 16):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

#      1
#    1 2 3
#  1 2 3 4 5
# piramis = int(input("Add hogy hány soros legyen a piramis: ")) 
# print("Piramis formában")
# for i in range(piramis):
#     for j in range(piramis - i - 1):
#         print(" ", end=" ")
#     for k in range(2 * i + 1):
#         print(k+1, end=" ")
#     print()

#        1
#      1 2 3
#     1 2 3 4
#      1 2 3
#        1
# rombusz = int(input("Add hogy hány soros legyen a rombusz: ")) 
# print("Rombusz formában")
# for i in range(rombusz):
#     for j in range(rombusz - i - 1):
#         print(" ", end=" ")
#     for k in range(2 * i + 1):
#         print(k+1, end=" ")
#     print()
# for i in range(rombusz -1):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for k in range(2*(rombusz - i - 1) - 1):
#         print(k+1, end=" ")
#     print()

# 1 2 3 4 5
#   1 2 3
#     1
#   1 2 3
# 1 2 3 4 5
# rombusz = int(input("Add hogy hány soros legyen a fordított rombusz: ")) 
# print("Rombusz fordítva formában")
# for i in range(rombusz -1 ):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(2 *(rombusz-i)-1):
#         print(k+1, end=" ")
#     print()
# for i in range(rombusz):
#     for j in range(rombusz - i - 1):
#         print(" ", end=" ")
#     for k in range(2 * i + 1):
#         print(k+1, end=" ")
#     print()

#    1 2     1 2
#  1 2 3 4 5 6 7 8
#    1 2 3 4 5 6
#      1 2 3 4
#        1 2
# sziv = 4
# print("Szív formában")
# for i in range(sziv//2, sziv, 2):
#     for j in range(1, sziv-i, 2):
#         print(" ", end=" ")
#     for j in range(i):
#         print(j+1, end=" ")
#     for j in range(1, sziv-i+1, 1):
#         print(" ", end=" ")
#     for j in range(i):
#         print(j+1, end=" ")
#     print()
# for i in range(sziv, 0, -1):
#     for j in range(i, sziv):
#         print(" ", end=" ")
#     for j in range(i*2):
#         print(j+1, end=" ")
#     print()

#szöveges lista elemeinek hosszának kiirása
#adj meg egy listát, amely szavakat tartalmaz
#és a program kiirja minden szó hosszát

szavak = ["alma", "kutya", "macska", "barack", "szendvics"]
index = 0
while index < len(szavak):
    word = szavak[index]
    print(f"A szó: {word}, a hossza: {len(word)}")
    index+=1