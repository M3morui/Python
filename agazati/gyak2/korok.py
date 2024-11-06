print("2.feladat")

def letrehoz():
    korok = []
    for i in range(5):
        szam = int(input("Adj meg egy kort[0,120]: "))
        korok.append(szam)
    return korok

def letreki(korok):
    print(" : ".join(map(str,korok)))

def elso_idos(korok):
    index = 0
    for kor in korok:
        if kor >= 70:
            index = korok.index(kor)
    return index

def konzolra_ir(index):
    print(f"Első idős ember korának a helye a listában: {index}.")

def fajl_ir(index):
    with open("oreg.txt", "w", encoding="UTF8") as file:
        file.write(f"Első idős ember korának a helye a listában: {index}.")

letre = letrehoz()
letki = letreki(letre)
elidos = elso_idos(letre)
kiir = konzolra_ir(elidos)
ir = fajl_ir(elidos)