feher_kenyer = 780 # Ft/kg
teljes_kiorlesu_kenyer = 1120 # Ft/kg

kenyer_tipus = input("Milyen kenyeret szeretne? (feher/teljes) : ").lower().strip()
try:
    mennyiseg = float(input("Mennyit szeretne vásárolni? (kg): ").strip())


except ValueError as error:
    print("Ne nyomkodd a CTRL + C -t :")

          ")
    print("Hibás mennyiség! Kérem, adjon meg egy számot.")
    print(f"Python mondja: {error}")
    exit()


if kenyer_tipus == "feher":
    print("A választott kenyér: Fehér kenyér. Mennyiség: {mennyiseg}kg")

    fizetendo = feher_kenyer * mennyiseg
elif kenyer_tipus == "teljes":
    print(f"A választott kenyér: Teljes kiörlésű kenyér. Mennyiség: {mennyiseg} kg.")
    fizetendo = teljes_kiorlesu_kenyer * mennyiseg 
else:
    print("Ismeretlen kenyér típus! Kérem válasszon a fehér vagy teljes kiörlésű közül.")
    exit() # Itt a vége kiléptünk
          
print(f"A fizetendő összeg: {fizetendo} Ft")




          
 
