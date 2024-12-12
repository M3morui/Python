import random
allatok = []

print("Add meg az 3 kedvenc állatodat!")

while len(allatok) < 3:
    allat = input(f"Adj meg egy kedvenc állatot: ")
    if allat not in allatok:
        allatok.append(allat)
        print(f"{len(allatok)} állat került hozzáadásra a listához")

print("\nA kedvenc állataid:")
print(", ".join(allatok))

legjobb_kedvenc = random.choice(allatok)

print(f"\nA kiválasztott kedvenc állat: {legjobb_kedvenc}")