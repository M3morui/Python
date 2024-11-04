#függvények#
# 1. írj egy fgv. amely két számot összead
def osszead(a, b):
    return a + b
print(f"1. feladat: {osszead(10,20)}")

# 2. írj egy fgv. amely vár három számot és a legnagyobbat adja vissza
def legnagyobb(a, b, c):
    return max(a, b, c)
print(f"2. feladat: {legnagyobb(10,15,5)}")

# 3. írj egy fgv. amely megmondja, hogy egy paraméterül adott szám páros v. páratlan
def parose(n = int(input("Adj meg egy számot: "))):
    if n % 2 == 0:
        print("Páros")
    else:
        print("Páratlan")
print(f"3. feladat: {parose()}")

# 4. írj egy fgv. amely visszaadja egy szöveg hosszát
def szoveg_hossza(s):
    return len(s)
print(f"4. feladat: {szoveg_hossza("Hello")}")

# 5. írj egy fgv. amely visszaadja egy lista elemeinek összegét!
def lista_osszege(l):
    szum = 0
    for e in l:
        szum += e
    return szum
print(f"5. feladat: {lista_osszege([1,2,3])}")

print("#"*50)

#szótárak#
# 1. hozz létre egy szótárat, amely tartalmazza a kedvenc gyümölcseidet és az árukat
gyumolcsok = {
    'eper': '500',
    'narancs': '300',
    'banán': '400',
    'alma': '100',
    'kiwi': '450', 
}
print(f"1. feladat {gyumolcsok}")
# 2. adj egy új gyümölcsöt a szótárba
gyumolcsok["szőlő"] = 600
print(f"2. feladat {gyumolcsok}")
# 3. listázd ki a szótárban található összes gyümölcs nevét
print(f"3. feladat {gyumolcsok.keys()}")
# 4. listázd ki a szótárban az összes gyümölcs árát
print(f"4. feladat {gyumolcsok.values()}")
# 5. számold ki a gyümölcsök összárát
print(f"5. feladat {sum(gyumolcsok.values())}")