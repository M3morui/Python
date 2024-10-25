penzed = int(input("Írd be, hogy mennyi pénzed van: "))
while penzed != 0:
    koltes = int(input("Mennyit szeretnél költeni belőle: "))
    print(f"Ennyi pénzed maradt: {penzed-koltes}")
    if koltes > penzed:
        print("Ennyit nem költhetsz, nincs ennyi pénzed!")
        ujpenzed = 0
        ujpenzed = penzed-koltes
        penzed = ujpenzed