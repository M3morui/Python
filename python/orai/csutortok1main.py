# 1 feladat
# pizza rendelő program.
# s méret 1500ft, m 2000ft, l 2500ft
# kérjük be milyen méretű a pizzát rendel
# ha nemjo a paraméter irja ki h ervénytelen
# irja ki a pizza árát

small_pizza = 1500
medium_pizza = 2000
large_pizza = 2500

pizza_sajt = 300
pizza_sonka = 200
pizza_kukorica = 150

price = 0
meret = False

while not meret:
    pizza = input("Válassz egy pizza méretet(S, M, L): ").upper()
    if pizza == "S":
        price += small_pizza
        meret = True
    elif pizza == "M":
        price += medium_pizza
        meret = True
    elif pizza == "L":
        price += large_pizza
        meret = True 
    else:
        print("Nem helyes értéket adtál meg!")

# #2 feladat
# #kérdezd meg h milyen feltétet szeretne
# # sajt plusz 300ft, sonka 200ft, kukorica 150ft
# #irja ki a program az összeget
feltett = True

while feltett:
    feltett = input("Kérsz feltétet(i/n): ")
    if feltett == "i":
        feltet = input("Válassz egy feltétet(sajt, sonka, kukorica): ")
        if feltet == "sajt":
            price += pizza_sajt
            feltett = True
        elif feltet == "sonka":
            price += pizza_sonka
            feltett = True
        elif feltet == "kukorica":
            price += pizza_kukorica
            feltett = True
        else:
            print("A feltét nem található.")
    else:
        feltett = False


print(f"Az általad választott pizza ára: {price} Ft")