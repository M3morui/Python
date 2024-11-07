print("3.feladat")

class Gombak:
    def beolvas(fajlkezeles):
        lista = []
        with open(fajlkezeles, "r", encoding="UTF8") as file:
            lines = file.readlines()
            for line in lines[1:]:
                line = line.strip()
                adat = line.split("@")

                neve = adat[0]
                nemzettseg = adat[1]
                evszak = adat[2]
                lista.append([neve, nemzettseg, evszak])
            return lista
        
    def gombak_szama(lista):
        print(f"A gombák száma: {len(lista)}")
    
    def papsapka(lista):
        for item in range(len(lista)):
            if lista[item][1] == "papsapkagombák ":
                print(f"Az első papsapkagomba neve: {lista[item][0]}")
                break

    def tinoru(lista):
        tinorug = []
        for item in lista:
            if item[1] == "tinóru":
                tinorug.append(item[1])
        print(f"A tinóru gombák száma: {len(tinorug)}")

    beolv = beolvas("gombak.txt")
    gombaksz = gombak_szama(beolv)
    sapka = papsapka(beolv)
    tin = tinoru(beolv)