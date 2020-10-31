with open("ChromosomeRegions.txt") as f:
    d = f.read()
    data = d.split("\n")
l = []
l.append(data[0])
for row in data:
    if "Promoter" in row:
        l.append(row)
with open('Results.txt', 'w') as f1:
    print(*l, sep="\n", file=f1)