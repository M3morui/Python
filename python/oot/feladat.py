class Konyvtar:
    def __init__(self):
        self.konyvek = []

    def hozzaad(self, elem):
        self.konyvek.append(elem)
        print(f"A könyvtárban található könyvek: ")
        print(f"{self.konyvek}")

    def akezd(self):
        db = 0
        for k in self.konyvek:
            if k.startswith("A"):
                print(f"{k}")
                db+=1
                print(f"{db} db könyv kedődik A-val.")



konyv = Konyvtar()
konyv.hozzaad("Egri csillagok")
konyv.hozzaad("A kőszívű ember fiai")
konyv.hozzaad("Harry Potter")
konyv.hozzaad("Alice csodaországban")
konyv.akezd()