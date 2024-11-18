class Szemely:
    def __init__(self, neve, kora, neme, nemzetisege, vallas="hindu"):
        self.neve = neve
        self.kora = kora
        self.neme = neme
        self.nemzetisege = nemzetisege
        self.vallas = vallas

class Alkalmazott(Szemely):
    tapasztalat = 4
    kepzettseg = "programozó"

Laci = Alkalmazott("Laci", 32, "férfi", "Magyar")
print(Laci.kepzettseg)
print(Laci.tapasztalat)