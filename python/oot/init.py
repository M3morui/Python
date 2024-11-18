# class Szemely:
#     def __init__(self, nev, kor, neme, nemzetiseg, vallas = "hindu"):
#         self.nev = nev
#         self.kor = kor
#         self.neme = neme
#         self.nemzetiseg = nemzetiseg
#         self.vallas = vallas

#     def kiir(self):
#         print(f"A neve: {self.nev}, kora: {self.kor}, Neme: {self.neme}, {self.nemzetiseg}, {self.vallas}")


#     def szabadsag(self):
#         if self.kopr <= 25:
#             return 10
#         elif self.kor <= 30:
#             return 15
#         elif self.kor >= 40:
#             return 20
    
    
#     def hello(self):
#         print("Hello", + self.nev)

# Kinga = Szemely("Kinga", 32, "nő", "Magyar")
# Tibi = Szemely("Tibi", 43, "férfi", "Magyar", "keresztény")
# print(Kinga.kor)
# print(Kinga.nemzetiseg)
# print(Kinga.vallas)
# print(Kinga.szabadsag())
# Kinga.kiir()
# Tibi.kiir()

# class Autok:
#     def __init__(self, marka, szine, rendszam, evjarat):
#         self.marka = marka
#         self.szine = szine
#         self.rendszam = rendszam
#         self.evjarat = evjarat

#     def kiir(self):
#         print(f"A kocsi márkája: {self.marka}, színe: {self.szine}, renszama: {self.rendszam}, eve: {self.evjarat}")

#     def evjaratEllenoriz(self):
#         if self.evjarat <= 2000:
#             return "Régi"
#         elif self.evjarat >= 2012:
#             return "Újabb"
#         elif self.evjarat >= 2022:
#             return "Új"

# Ford = Autok("Ford", "kék", "AA432V", 2012)
# Ford.kiir()
# print(Ford.evjaratEllenoriz)

# osztály neve haziallat
# tipusa neve kora szore
# 3 peldanyt hozz letre
#2venel fiatalabb kolyok, 2 eves vagy idosebb felnott, 7eves vagy idosebb oreg

class Haziallat:
    def __init__(self, tipusa, neve, kora, szore):
        self.tipusa = tipusa
        self.neve = neve
        self.kora = kora
        self.szore = szore

    def kiir(self):
        print(f"A kutya típusa: {self.tipusa}, neve: {self.neve}, kora: {self.kora}, szore: {self.szore}")

    def kutyaidos(self):
        if self.kora < 2:
            return "Kölyök"
        elif self.kora <= 7:
            return "Felnőtt"
        elif self.kora > 7:
            return "Senior"

Sanyi = Haziallat("Kutya", "Sanyi", 9, "barna")
Gaspar = Haziallat("Macska", "Gáspár", 1, "cirmos")
Jonas = Haziallat("Macska", "Jónás", 4, "fekete")
Sanyi.kiir()
Gaspar.kiir()
Jonas.kiir()
print(Sanyi.kutyaidos())
print(Gaspar.kutyaidos())
print(Jonas.kutyaidos())