class Szemely:
    nev = ""
    kor = None
    neme = ""

    def set_nev(self,value):
        self.nev = value

    def set_kor(self,value):
        self.kor = value

sz1 = Szemely
sz1.set_nev("Kinga")
sz1.set_kor(34)
print(sz1.nev)
print(sz1.kor)