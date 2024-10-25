penzed = int(input("Írd be, hogy mennyi pénzed van: "))
while penzed != 0:
    koltes = int(input("Mennyit szeretnél költeni belőle: "))
    if koltes < penzed:
        print(f"Ennyi pénzed maradt: {penzed-koltes}")
        ujpenzed = 0
        ujpenzed = penzed-koltes
        penzed = ujpenzed
    elif koltes > penzed:
        print("Ennyit nem költhetsz, nincs ennyi pénzed!")
    else:
        print(f"Ennyi pénzed maradt: {penzed-koltes}")
        break