# 1.Feladat
# Készíts egy programot amivel a megadott listából ki kell választani melyek azok a szavak,
# amelyek hosszúságának az értéke 5 és ki kell íratni a konzolra melyek ezek a szavak 
# és hány darab van belőlük.

szavak = [
    "alma", "asztal", "doboz", "ceruza", "egér", "fotel",   # 5 betűs szavak (azonos hosszúságú)
    "szék", "pohár", "táblázat", "könyv", "kulcs", "karkötő",
    "mobiltelefon", "számítógép", "egérpad", "monitor", "hangszóró", "szék",
    "asztalterítő", "függöny", "szőnyeg", "párna", "papucs", "cipőfűző",
    "naptár", "hűtőszekrény", "mosogatógép", "főzőlap", "mikrohullámú",
    "nyomtató", "scanner", "projektor", "távirányító", "szendvics",
    "tolltartó", "jegyzetfüzet", "irattartó", "mappa", "papír",
    "töltőtoll", "hegyező", "ragasztószalag", "füzet", "kapocs",
    "toll", "filctoll", "színesceruza", "vonalzó", "radír"
]

ot_hosszu = []
for i in szavak:
    if len(i) == 5:
        ot_hosszu.append(i)
print(f"Az öt betűs szavak listája: {ot_hosszu}, {len(ot_hosszu)} db van a listában.")

# 2.Feladat
# Kérj be születési évszámokat és számold ki a kort és azt add a listához. 
# Írd ki a konzolra, hány db év szerepel és melyik a legnagyobb kor a listában.

most = 2024
evek = []
kor = []
ev = False
while not ev:
    szuletesiev = int(input("Adj meg születési évszámokat: "))
    evek.append(szuletesiev)
    kor.append(most-szuletesiev)
    meg = input("Szeretnél még megadni évet? ")
    if meg != "i":
        ev = True
print(f"Összesen {len(evek)} év van, a legnagyobb kor: {max(kor)}")