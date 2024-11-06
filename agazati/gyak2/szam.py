print("1.feladat")

import random

szam = random.randint(1, 50)
print(f"A generált szám: {szam}")

if szam % 5 == 0 and szam % 3 == 0:
    print("A szám öttel és hárommal is osztható!")
elif szam % 5 == 0:
    print("A szám öttel osztható!")
elif szam % 3 == 0:
    print("A szám hárommal osztható!")
