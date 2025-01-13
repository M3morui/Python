valuta = input("Milyen valutáról szeretne átváltani? ").upper()

if valuta == "USD":
    osszeg = int(input("Adja meg az átváltandó összeget: "))
    eredmeny = osszeg*360
    print(f"Az átváltott összeg eredménye: {eredmeny} HUF")

if valuta == "EUR":
    osszeg = int(input("Adja meg az átváltandó összeget: "))
    eredmeny = osszeg*400
    print(f"Az átváltott összeg eredménye: {eredmeny} HUF")