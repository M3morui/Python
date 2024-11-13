import random

def jotermes(szam):
    return szam >= 5

gyumolcsfak=["almafa","szilvafa","eperfa","körtefa","barackfa","cseresznyefa"]
gyumolcsfak.append("diófa")

termesek = []
jotermesszamolas = 0
for gyumolcs in gyumolcsfak:
    termes = random.randint(1, 11)
    termesek.append(termes)
    if jotermes(termes):
        jotermesszamolas += 1
    print(f"{gyumolcs} - {termes} db termés")

print(f"Összesen {sum(termesek)} db termés volt a kertben.")
print(f"Átlagosan {round(sum(termesek)/len(termesek))} db termés volt a fákon.")
print(f"A kertben {jotermesszamolas} db fa volt, ami elegendő (jó) termést hozott.")