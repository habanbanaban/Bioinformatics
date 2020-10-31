with open("Genes.fa") as f:
    a = f.read()
    d = a.split("\n")
colnames = ["GeneID", "Sequence Length", "Start Codon"]
l1 = []
l2 = []
l3 = []
length = 0
start_codon = False
for element in d:
    if element.startswith(">"):
        l1.append(element.split(" ")[0])
        for element in d[d.index(element)+1:]:
            if element.startswith(">"):
                break
            else:
                length += len(element)
            if "ATG" in element:
                start_codon = True
        l2.append(length)
        length = 0
        l3.append(start_codon)
        start_codon = False


with open("fastadone.csv", "w") as outfile:
    outfile.write(",".join(colnames) + "\n")
    for i in range(len(l1)):
        outfile.write(f"{l1[i]},{l2[i]},{l3[i]}\n")