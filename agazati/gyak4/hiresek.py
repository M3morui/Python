hires = []
for i in range(3):
    nevv = input("Add meg egy híres nő nevét! ")
    foglalkozass = input("Add meg a foglalkozását! ")
    nemzet = input("Add meg a nemzetiségét (a/n)! ")

    if nemzet == "a":
        nevv = "Ms. " + nevv
    else:
        nevv = "Frau " + nevv
    
    hires.append([nevv, foglalkozass])

for item in hires:
    print(f"{item[0]} egy híres {item[1]}")