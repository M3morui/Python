class Zoldsegek:
    def __init__(self):
        self.lista = []

    def beolvasas(self):
        with open("zoldsegek.txt", "r", encoding="UTF8") as file:
            adatok = file.readlines()

            for adat in adatok:
                adat = adat.strip()
                adat = adat.split(";")

                zoldseg = adat[0]
                tonna = int(adat[1])
                ar = int(adat[2])
                ev = int(adat[3])

                self.lista.append([zoldseg, tonna, ar, ev])

            print("A teljes fájl tartalma:")
            for list in self.lista:
                print(f"{list[0]} - {list[1]} tonna - {list[2]} Ft/kg - {list[3]}")

    def termesuk_2015_utan(self):
        print("\n2015 utáni zöldségek:")
        for termes in self.lista:
            if termes[3] > 2015:
                print(f"{termes[0]} - {termes[1]} tonna - {termes[2]} Ft/kg - {termes[3]}")

    def legolcsobb(self):
        legolcsobb = float("inf")
        legolcsobbzoldseg = " "
        print("\nA legolcsóbb zöldség:")
        for olcso in self.lista:
            if olcso[2] < legolcsobb:
                legolcsobb = olcso[2]
                legolcsobbzoldseg = olcso[0]

        print(f"{legolcsobbzoldseg} - {legolcsobb} Ft/kg.\n")

    def paprika_kezdes(self):
        with open("paprika_zoldsegek.txt", "w", encoding="UTF8") as fajl:

            megszamol = 0
            for kezdodik in self.lista:
                if kezdodik[0].startswith("Paprika"):
                    megszamol += 1
                    print(f"{kezdodik[0]} - {kezdodik[1]} tonna - {kezdodik[2]} Ft/kg - {kezdodik[3]}")

                    fajl.write(f"\n{kezdodik[0]} - {kezdodik[1]} tonna - {kezdodik[2]} Ft/kg - {kezdodik[3]}")

            print(f"\n'Paprika'-val kezdődő zöldségek száma: {megszamol}")
            fajl.write(f"\n'Paprika'-val kezdődő zöldségek száma: {megszamol}")
            print("\nA paprika_zoldsegek.txt fájlba kiírásra kerültek az adatok.")

etelek = Zoldsegek()
etelek.beolvasas()
etelek.termesuk_2015_utan()
etelek.legolcsobb()
etelek.paprika_kezdes()