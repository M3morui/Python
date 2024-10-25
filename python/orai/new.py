import datetime as dt

today = dt.date.today()
now = dt.datetime.now()

print(now)


# mai nap komplett Év-Hónap_Nap formatumban

# Év
print(today.year)

# Hónap
print(today.month)

# Nap
new_years_eve = dt.datetime(2024,10,26,23,59,59,)

print(new_years_eve)

today = dt.datetime.now()

