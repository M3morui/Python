def beolvas(fajlkezeles):
    lista = []
    with open (fajlkezeles, "r", encoding="UTF8") as file:
        lines = file.readlines()

        for line in lines[1:]:
            line = line.strip()
            adat = line.split("#")

            szelesseg = int(adat[0])
            magassag = int(adat[1])
            melyseg = int(adat[2])
            suly = int(adat[3])
            lista.append([szelesseg, magassag, melyseg, suly])
        return lista
        # for item in lista:
        #     print(f"{item[0]}, {item[1]},  {item[2]}, {item[3]}")

def pogyaszok_szama(lista):
    print(f"A pogyászok száma: {len(lista)}")

def atlag(lista):
    sulyok = []
    for item in lista:
        if item[0] == 51:
            sulyok.append(item[3])
    print(f"Az 51 cm-es pogyászok átlag súlyértéke: {round((sum(sulyok)/len(sulyok))*1000)} g")

def legmagasabb_pogyasz(lista):
    legm = 0
    legszelesebb = 0
    legmely = 0
    legsuly = 0
    for item in lista:
        if item[1] > legm:
            legm = item[1]
            legszelesebb = item[0]
            legmely = item[2]
            legsuly = item[3]
    print(f"A legmagasabb pogyász méretei: {legszelesebb}x{legm}x{legmely}, súlya: {legsuly} kg.")

beolv = beolvas("csomag.txt")
pogy_szam = pogyaszok_szama(beolv)
a = atlag(beolv)
legmagasabb = legmagasabb_pogyasz(beolv)