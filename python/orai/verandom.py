import random

nyert = False
while not nyert:
    gep = random.randint(1,5)
    szam = int(input("Adj meg egy számot 1 és 5 között: "))
    if gep > szam:
        print("Kisebb számot adtál meg.")
        print(f"A gép által megadott szám: {gep},  a te számod: {szam}.")
    elif gep < szam:
        print("Nagyobb számot adtál meg.")
        print(f"A gép által megadott szám: {gep},  a te számod: {szam}.")
    elif gep == szam:
        print("Eltaláltad!")
        print(f"A gép által megadott szám: {gep},  a te számod: {szam}.")
        nyert = True

