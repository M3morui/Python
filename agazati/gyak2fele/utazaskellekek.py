import random
kellekek = []

while len(kellekek) < 7:
    kellek = input(f"Kérem adja meg az utazási kellékek nevét ({len(kellekek) + 1}): ")
    kellekek.append(kellek)
    print(f"{len(kellekek)}. {kellek} hozzáadva a listához.")

print("A megadott kellékek: ")
index = 1
for kellek in kellekek:
    print(f"{index}. {kellek}")
    index +=1

kovetkezo_kellek = random.choice(kellekek)
print(f"Fontos utazási kellék: {kovetkezo_kellek}")