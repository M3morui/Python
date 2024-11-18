import random
celpontok = []

while len(celpontok) < 4:
    celpont = input(f"Kérem adja meg az űrutazási célpont nevét ({len(celpontok) + 1}): ")
    celpontok.append(celpont)
    print(f"{len(celpontok)}. {celpont} hozzáadva a listához.")

print("A lehetséges célpontok: ")
index = 1
for celpont in celpontok:
    print(f"{index}. célpont: {celpont}")
    index +=1

kovetkezo_celpont = random.choice(celpontok)
print(f"A következő űrutazás célpontja: {kovetkezo_celpont}")