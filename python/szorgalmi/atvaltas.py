egyseg = input("Milyen mértékegységben adod meg: ").upper()
# 1GB = 1024MB
atvaltas = int(input("Írd be az átváltandó számot: "))
if egyseg == "MB":
    print(f"Az eredmény: {atvaltas / 1024} GB")
elif egyseg == "GB":
    print(f"Az eredmény: {atvaltas*1024} MB")