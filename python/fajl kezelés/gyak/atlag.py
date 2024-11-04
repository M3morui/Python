lista = []
oszt_atlag = []
with open("atlag.txt", "r", encoding="UTF8") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        adat = line.split(";")

        nev = adat[0]
        atlag = float(adat[1])
        lista.append([nev,atlag])

for item in lista:
    # print(f"{item[0]}, {item[1]}")
    oszt_atlag.append(item[1])
    if item[0].startswith("K"):
        # print(item[0])
        print(f"{item[0]}, {item[1]}")

print(f"Az ostály átlaga: {round(sum(oszt_atlag)/len(oszt_atlag),2)}")
