lista = []
sample_set = {2, 3, 4,1, 5} #rendezett halmaz
print(sample_set)
sample_set.add(10)
print(sample_set)
sample_set.update([11, 12])
print(sample_set)
print(len(sample_set))
tartalmazza = 11 in sample_set
nem_tartalmazza = 18 in sample_set
print(tartalmazza)
print(nem_tartalmazza)
for szam in sample_set:
    print(szam)

auto_markak = [ "Ford", "Tesla", "BMW", "Ford", "Toyota", "Mazda", "Tesla", "BMW", "Honda", "Toyota", "Tesla", "Ferrari", "Mazda", "Porsche"]
print(auto_markak)
# auto_halmaz =  {"Ford"}
# auto_halmaz.update(auto_markak)
auto_halmaz = set(auto_markak)
print(auto_halmaz)

auto_halmaz.remove("Porsche") #eltávolit de ha nincs benn error
print("Eltávolítás után: ", auto_halmaz)
auto_halmaz.discard("Porsche") #eltavolit de nem ir errort ha nincs benne
