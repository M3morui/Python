fajl = open('szamok.txt', 'w')
for i in range(10):
    sor = [str(i*10 +i1) for i1 in range(1, 11)]
    print(' '.join(sor), file=fajl)
fajl.close()

with open('data.txt', 'w') as file:
    file.write('Első sor.\n')
    file.write('Második sor.\n')
    file.write('Harmadik sor.\n')