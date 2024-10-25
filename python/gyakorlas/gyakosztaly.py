# készets egy programot amelyben két osztályt hozunk létre:
# diák és jegyzet. a program célja hogy lehetőséget adjon a diákok
# hozzáadására, jegyek rögzítésére, valamint az átlag kiszámítására

# diák osztály: attr.: nev, jegyek. metod.: uj_jegy(jegy), atlag()
# jegyzet osztály: attr.: diakok. metod.: uj_diak(diak), atlagok_osszege(),
#                                         osszes_diak_atlaga()

class Diak:
    def __init__(self, nev):
        self.nev = nev
        self.jegyek = []

    def uj_jegy(self, jegy):
        self.jegyek.append(jegy)

    def atlag(self):
        if not self.jegyek:
            return 0
        return sum(self.jegyek) / len(self.jegyek)

class Jegyzet:
    def __init__(self):
        self.diakok = []

    def uj_diak(self, diak):
        self.diakok.append(diak)

    def atlagok_osszege(self):
        return sum(diak.atlag() for diak in self.diakok)
    
    def osszes_diak_atlaga(self):
        if not self.diakok:
            return 0
        return self.atlagok_osszege() / len(self.diakok)

def main():
    diak1 = Diak("Anna")
    diak2 = Diak("Béla")

    diak1.uj_jegy(4)
    diak1.uj_jegy(3)
    diak1.uj_jegy(5)

    diak2.uj_jegy(1)
    diak2.uj_jegy(3)
    diak2.uj_jegy(5)

    jegyzet = Jegyzet()
    jegyzet.uj_diak(diak1)
    jegyzet.uj_diak(diak2)

    print(f"Anna átlaga: {diak1.atlag()}")
    print(f"Béla átlaga: {diak2.atlag()}")
    print(f"Átlagok összege: {jegyzet.atlagok_osszege()}")
    print(f"Összes diák átlaga: {jegyzet.osszes_diak_atlaga()}")

if __name__ == "__main__":
    main()