# class Szemely:
#     def __init__(self, neve, kora, neme, nemzetisege, vallas="hindu"):
#         self.neve = neve
#         self.kora = kora
#         self.neme = neme
#         self.nemzetisege = nemzetisege
#         self.vallas = vallas
    
# class Alkalmazott(Szemely):
#     def __init__(self, neve, kora, neme, nemzetisege, vallas, tapasztalat, kepzettseg):
#         super().__init__(neve, kora, neme, nemzetisege, vallas)
#         self.tapasztalat = tapasztalat
#         self.kepzettseg = kepzettseg

#     def kiir(self):
#         print(f"Az alkalmazott neve: {self.neve}, tapasztalata: {self.tapasztalat} év, képzettség: {self.kepzettseg}")

#     def tobbtapasztalat(self):
#         if self.tapasztalat <= 10:
#             return "Medior"
#         elif self.tapasztalat <= 5:
#             return "Junior"
#         elif self.tapasztalat > 10:
#             return "Senior"

# Kinga = Alkalmazott("Kinga", 32, "nő", "Magyar", "pogány", 5, "programozó")
# Laci = Alkalmazott("Laci", 52, "férfi", "Magyar" "keresztény", 20, "programozó")
# print(Kinga.neme)
# Kinga.kiir()
# print(f"A {Kinga.neve} tapasztalati szintje: {Kinga.tobbtapasztalat()}")
# print(f"A {Laci.neve} tapasztalati szintje: {Laci.tobbtapasztalat()}")

# class Autok:
#     def __init__(self, marka, szine, ar, rendszam):
#         self.marka = marka
#         self.szine = szine
#         self.ar = ar
#         self.rendszam = rendszam

# class Auto_kereskedes(Autok):
#     def __init__(self, marka, szine, ar, rendszam, eladas, ertekesito):
#         super().__init__(marka, szine, ar, rendszam)
#         self.eladas = eladas
#         self.ertekesito = ertekesito

    
#     def kiir(self):
#         print(f"Az autó márkája: {self.marka}, színe: {self.szine}, ára: {self.ar}, renszáma: {self.rendszam}, eladott mennyiség: {self.eladas}, értékesítő: {self.ertekesito}")

# auto1 = Auto_kereskedes("Ford", "szürke", 1500000, "AA4521", 10, "John")
# print(auto1.marka)
# auto1.kiir()


# szulo osztaly: diak,neve,szulketesidatum,email,telefonszam
# gyerekosztaly: osztaly,osztalyletszam, osztalyfonok,tanulmanyiatlag
# kiirásra hozzatok létre metódust
class Diak:
    def __init__(self, neve, szuletes, email, telszam):
        self.neve = neve
        self.szuletes = szuletes
        self.email = email
        self.telszam = telszam

class Osztaly(Diak):
    def __init__(self, neve, szuletes, email, telszam, oszifo, atlag):
        super().__init__(neve, szuletes, email, telszam)
        self.oszifo = oszifo
        self.atlag = atlag

    def kiir(self):
        print(f"A diak neve: {self.neve}, születési dátum: {self.szueletes}, email: {self.email}, telefonszama: {self.telszam}, osztrályfőnök: {self.oszifo}, atlag: {self.atlag}")

diak1 = Osztaly("Tibi", "1991.01.01", "tibi@gmail.com", "06602346677", "Csíra", "3,5")
diak1.kiir()