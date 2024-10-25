# key --- value
# redavid = ["Rédai Dávid", 1994, 0]
# feisti = ["Fekete István", 2002, 0]
# nagya = ["Nagy Anna", 2001, 1]
database = {
    'redavid': 'Rédai Dávid',
    'feisti': 'Fekete István',
    'nagya': 'Nagy Anna'
}
# print("Adatok száma: ", len(database))
# print('redavid' in database)

# database.update({'nagya': 'Fekete-Nagy Anna'})
# print(database)

for data in database.keys():
    print(data + " = " + database[data])
