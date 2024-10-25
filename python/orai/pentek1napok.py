import datetime as dt

today = dt.date.today()

print(today)

print(f"Nap: {today.day}")
print(f"Hónap: {today.month}")
print(f"Év: {today.year}")

ido = dt.datetime.now()
print(ido)

ujev = dt.datetime(2024,12,31,23,59)
print(ujev)

mainap = dt.datetime(2024,9,13,23,59)
print(mainap)

napok_hatra = ujev - mainap
print(napok_hatra)

nap2 = dt.date(2024,9,13)
ujertek2 = dt.timedelta(days=109)
print(nap2 + ujertek2)

kezdo_idopont = dt.datetime(2024,9,13,8,38,0)
befejezes_idopont = dt.datetime(2024,9,13,13,30,0)
szamitas = befejezes_idopont - kezdo_idopont
print(szamitas)
print(type(kezdo_idopont))
print(type(befejezes_idopont))
print(type(szamitas))

most = dt.datetime.now()
szuletesnap = dt.datetime(2003,3,20,20,30)
kalkulacio = most - szuletesnap
print(kalkulacio)

now = dt.datetime.now()
print(f"{now}")
print(f"{now:%H:%M:%S}")