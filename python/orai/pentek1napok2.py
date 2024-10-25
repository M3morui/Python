import datetime as dt

mainap = dt.date.today()
szuletesi_datum = dt.date(2003,3,20)
delta_kor = mainap - szuletesi_datum
delta_kor_nap = delta_kor.days
ev = delta_kor_nap // 365
honap = (delta_kor_nap % 365) // 30
print(f"Te ennyi {ev} éves vagy és {honap} hónapos.")