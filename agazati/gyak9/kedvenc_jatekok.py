import random

videojatek = []

while len(videojatek) < 4:
    jatek = input("Add meg 4 kedvenc videójátékodat! ")
    videojatek.append(jatek)
    print(f"{len(videojatek)}. játék: {jatek}")

print("\nA kedvenc videójátékaid: ")
print(", ".join(map(str,videojatek)))

evjatek = random.choice(videojatek)
print(f"\nA 2025 év játéka: {evjatek}")