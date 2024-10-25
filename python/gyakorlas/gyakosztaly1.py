class Auto:
    def __init__(self, marka, ev, ar):
        self.marka = marka
        self.ev = ev
        self.ar = ar

    def auto_adatai(self):
        return self.marka, self.ev, self.ar

class Garazs:
    def __init__(self):
        self.autok =[]
    
    def uj_auto(self, auto):
        self.autok.append(auto)
    
    def autos_lista(self):
        return [auto.auto_adatai() for auto in self.autok]
    
    def osszertek(self):
        return sum(auto.ar for auto in self.autok)
    
