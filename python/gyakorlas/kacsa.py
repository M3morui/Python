# kacsa kereső

# Írd meg a beolvs() metódust, ami egy szöveg típusú paramétert vár,
# ami a fajl neve.

# A feladat, hogy olvasd be a fájl tartalmát,
# ami soronként egy szöveget, egy lebegőpontos számot,
# majd egy egész számot tartalmaz, pontosvesszővel elválasztva.

# A sorokból alkoss egy listát, ami dictionaryket tartalmaz a
# lenti táblázatban látható a kulcs érték párokkal. Térj vissza a megalkotott listával.

# szin | szöveg | kacsa színe
# meret | lebegopontos | kacsa merete
# sebesseg | szam | kacsa sebessege

"""
[{szin: k, meret: 10.1, sebesseg: 2}, {szin: f, meret: 3.5, sebesseg: 1}, {...}]

be.txt

k;10.1;2
f;3.5;1
z;20.4;11
"""

def beolvas(szoveg):
    lista = []
    with open(szoveg, "r", encoding="UTF-8") as file:
        for line in file:
            data = line.strip().split(";")
            lista.append({"szin":data[0], "meret":float(data[1]), "sebesseg":int(data[2])})
    return lista

pelda = beolvas("be.txt")

for i in pelda:
    print(i)