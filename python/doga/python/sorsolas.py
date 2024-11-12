import random

nevek = []

while len(nevek) < 5:
    nev = input(f"Kérem adja meg a(z) {len(nevek) + 1} nevet: ")
    nevek.append(nev)
    print(f"{len(nevek)}. név: {nev} hozzáadva a listához.")

for nev in nevek:
    
    szamlalo += 1

    print(f"{szamlalo}. {nev}")


nyertes = random.choice(nevek)
print(f"Asorsolás nyertese: {nyertes}")

