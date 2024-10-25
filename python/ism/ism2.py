import datetime as dt

# today = dt.date.today()
# birthdate = dt.date(2003,3,20)

# delta_age = (today-birthdate)
# day_old = delta_age.days
# years = day_old // 365

# months = (day_old % 365) // 30
# print(f"Te ennyi {years} éves vagy és {months} hónapos.")


ma = dt.date.today()
print(ma)
print(ma.year)
print(ma.month)
print(ma.day)

ejfel = dt.time()
print(ejfel)
most = dt.datetime.now()
print(most)

ujev = dt.datetime(2024,12,31,23,59,59)
print(ujev)

kettokozott = most - ujev
print(kettokozott)

egyhet = dt.timedelta(days=7)
print(most+egyhet)