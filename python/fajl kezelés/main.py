# 1.feladat
# pénz feldobás fej vagy írás
# eredményt írasd ki txt fájlban

# F I I F I
# Kérek egy tippet (F/I): F
# A tipp F, a dobás eredménye I volt
# Ön nem találta el

import random

dobas = ["F", "I"]
dobasok = []
for i in range(5):
    dob = random.choice(dobas)
    dobasok.append(dob)
print(" ".join(dobasok))
feldobas = random.choice(dobasok)
tipp = input("Kérek egy tippet (F/I): ").upper()
with open("penzdobas.txt", "a") as file:
    file.write(f"A tipp {tipp}, a dobás eredménye {feldobas} volt.")
    if tipp == feldobas:
        file.write("Eltaláltad!")
        print("Eltaláltad!")
    else:
        file.write("Nem találtad el!")
        print("Nem találtad el!")