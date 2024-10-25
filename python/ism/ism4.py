#ASCII
# print(ord("A"))
# print(chr(65))

# for i in range(97, 123):
#     print(f"{i} => {chr(i)}")

# for n in range(1, 10):
#     print(n)

# for i in "naplemente":
#     print(ord(i))

# count=0
# for x in "naplemente":
#     if x == "e":
#         count+=1
# print(f"Van benne {count} darab 'e' betű.")

# for lista in ["Macska", "Egér", "Kutya"]:
#     print(lista)

# print("A hét törpe:")
# het_torpe = ["Tudor", "Vidor", "Morgó", "Szundi", "Szende", "Hapci", "Kuka"]
# for torp in het_torpe:
#     print("\t -"+torp)
# print("\t és Hófehérke")

lista = ["Első", "Második", "Harmadik"]
for kulso in lista:
    print(kulso)
    for belso in range(3):
        print(f"\t {belso + 1}")
print("Kész...")