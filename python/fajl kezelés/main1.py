names = []
with open("nevek.txt", "r") as file:
    lines = file.readline().split(";")

for line in lines:
    line = line.strip()
    names.append(line)
names.sort()
print(" ".join(names))

with open("rendezett_nevek.txt", "w") as file:
    file.write("; ".join(names))