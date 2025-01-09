import random

allatok = []
print("Add meg az 3 kedvenc állatodat!")
db = 0
while len(allatok) < 3:
    allat = input("Adj meg egy kedvenc állatot: ")
    allatok.append(allat)
    db+=1
    print(f"{db} állat került hozzáadásra a listához.")

print("\nA kedvenc állataid:") 
print(", ".join(map(str,allatok)))

kivalasztottallat = random.choice(allatok)
print(f"\nA kiválasztott kedvenc állat: {kivalasztottallat}")