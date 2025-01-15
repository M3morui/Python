class Bolt:
    def __init__(self):
        self.lista = []

    def beolvasas(self):
        with open("termekek.txt", "r", encoding="UTF8") as file:
            adatok = file. readlines()

            for adat in adatok[1:]:
                adat = adat.strip()
                adat = adat.split(";")

                nev = adat[0]
                ar = int(adat[1])
                eladott = int(adat[2])
                ev = int(adat[3])

                self.lista.append([nev, ar, eladott, ev])
            print("A fájl tartalma:\n")
            for list in self.lista:
                print(f"{list[0]};{list[1]};{list[2]};{list[3]}")

    def legdragabb(self):
        legdragabb = 0
        legdragabbtermek = " "
        for draga in self.lista:
            if draga[1] > legdragabb:
                legdragabb = draga[1]
                legdragabbtermek = draga[0]
        print(f"A legdrágább termék: {legdragabbtermek} ({legdragabb} Ft)")

    def atlag(self):
        db_atlaga = []
        for a in self.lista:
            db_atlaga.append(a[2])
        print(f"Az eladott termékek darabszámának átlaga: {round(sum(db_atlaga)/len(db_atlaga))}")

    def ckezd(self):
        megszamol = 0
        with open("C_betu_termekek.txt", "w", encoding="UTF8") as fajl:
            for c in self.lista:
                if c[0].startswith("C"):
                    megszamol += 1  
                    fajl.write(f'\n"C"-vel kezdődő termékek: {c[0]};{c[1]};{c[2]};{c[3]};')
                    print(f'"C"-vel kezdődő termékek: {c[0]};{c[1]};{c[2]};{c[3]};')
            fajl.write(f'\n"C"-vel kezdődő termékek száma: {megszamol}')
            print(f'"C"-vel kezdődő termékek száma: {megszamol}')
                

muvesz = Bolt()
muvesz.beolvasas()
muvesz.legdragabb()
muvesz.atlag()
muvesz.ckezd()