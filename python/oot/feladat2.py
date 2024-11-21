class Jatekos:
    def __init__(self, nev):
        self.nev = nev
        self.pontszam = 0

    def novel(self,pont):
        self.pontszam += pont
        
    def kiir(self):
        print(f"{self.nev}, {self.pontszam}")
    
    def csokken(self, levonas):
        result = self.pontszam - levonas
        if result > 0:
            print(f"{self.nev} pontszáma: {result}")
        else:
            print(f"{self.nev} pontszáma nem lehet negatív!")

jatekos1 = Jatekos("John")
jatekos1.novel(4)
jatekos1.novel(10)
jatekos1.novel(8)
jatekos1.kiir()
jatekos1.csokken(5)