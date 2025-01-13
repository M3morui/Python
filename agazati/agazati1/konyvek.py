class Konyvek:
    def __init__(self):
        self.lista = []

    def beolvasas(self):
        with open("konyvek.txt", "r", encoding="UTF8") as file:
            adatok = file.readlines()

            for adat in adatok[1:]:
                adat = adat.strip()
                adat = adat.split(";")

                cim = adat[0]
                ar = int(adat[1])
                eladott = int(adat[2])
                ev = int(adat[3])

                self.lista.append([cim, ar, eladott, ev])
            print("A könyvek listája:\n")
            for list in self.lista:
                print(f"{list[0]};{list[1]};{list[2]};{list[3]}\n")

    def utan(self):
        print("2010 után megjelent könyvek:\n")
        for i in self.lista:
            if i[3] > 2010:
                print(f"{i[0]};{i[1]};{i[2]};{i[3]}")
    
    def legolcsobb(self):
        legolcsobb = float("inf")
        legolcsobbkonyv = " "
        for olcso in self.lista:
            if olcso[1] < legolcsobb:
                legolcsobb = olcso[1]
                legolcsobbkonyv = olcso[0]
        print(f"\nA legolcsóbb könyv: {legolcsobbkonyv} {legolcsobb} Ft\n")
    
    def hpkonyvek(self):
        print("Harry Potter könyvek kiírva a fájlba:")
        with open("HarryPotter_konyvek.txt", "w", encoding="UTF8") as fajl:
            for hp in self.lista:
                if hp[0].startswith("Harry Potter"):
                    print(f"\n{hp[0]}")
                    fajl.write(f"{hp[0]}\n")

konyv = Konyvek()
konyv.beolvasas()
konyv.utan()
konyv.legolcsobb()
konyv.hpkonyvek()