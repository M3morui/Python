class Allatkert:
    def __init__(self):
        self.allatok = []

    def hozzaad(self, elem):
        self.allatok.append(elem)

    def kiir(self):
        print(self.allatok)
        print(f"Állatok száma: {len(self.allatok)}")
    
    def tigriszam(self):
        db = 0
        for i in self.allatok:
            if i == "Tigris":
                db += 1
        print(f"A tigrisek száma: {db}")

allat = Allatkert()
allat.hozzaad("Oroszlán")
allat.hozzaad("Elefánt")
allat.hozzaad("Tigris")
allat.hozzaad("Tigris")
allat.hozzaad("Tigris")
allat.kiir()
allat.tigriszam()