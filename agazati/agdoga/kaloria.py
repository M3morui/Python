tabor = input("Adja meg a tábor nevét : ")
kaloria = []
print("Adja meg az egyes napok elégetett kalóriáit!")
print("Legalább 5 nap adatait meg kell adnia.")
while len(kaloria) < 5:
    elkaloria = int(input(f"Adjon meg egy napi kalóriaértéket (jelenlegi adatok száma: {len(kaloria)}): "))
    kaloria.append(elkaloria)

    if len(kaloria) >= 5:
        meg = input("Szeretne további kalóriákat hozzáadni? (i/n): ")
        if meg == "n":
            break
        elif meg == "i":
            elkaloria = int(input(f"Adjon meg egy napi kalóriaértéket (jelenlegi adatok száma: {len(kaloria)}): "))


    

print("===== Heti Kalóriaösszegzés =====")
print(f"Tábor neve: {tabor}")
print(f"Átlagosan elégetett kalória naponta: {round(sum(kaloria)/len(kaloria))} kcal")