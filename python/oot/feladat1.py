class Bevasarlolista:
    def __init__(self):
        self.lista = []

    def hozzaad(self, elem):
        self.lista.append(elem)
        print(f"A bevásárló lista tartalma: {self.lista}")

    def eltavolit(self):
        self.lista.remove("Tej")
        print(f"A bevásárló lista tartalma: {self.lista}")

    def tartalmaz(self):
        for i in self.lista:
            if i == "Vaj":
                print("A keresett elem megtalálható a listában.")
            else:
                ("Még nem írtad fel.")


bevasarlas = Bevasarlolista()
bevasarlas.hozzaad("Kenyér")
bevasarlas.hozzaad("Tej")
bevasarlas.hozzaad("Vaj")
bevasarlas.eltavolit()
bevasarlas.tartalmaz()