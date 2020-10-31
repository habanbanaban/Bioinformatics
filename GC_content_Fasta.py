#C:\Users\User\Documents\Bioinformatics\gene.fa

def gc_content(file_dir):
    nucleotides = ""
    with open(file_dir) as gene_file:
        for line in gene_file.readlines()[1:]:
            nucleotides += line.strip()
    GC = 0
    for element in nucleotides:
        for char in element:
            if char == "G":
                GC += 1
            elif char == "C":
                GC += 1
    return(GC/len(nucleotides) * 100)

file_dir = input("input file path: ")
print(f"The GC content of this gene is: {round(gc_content(file_dir),2)}%")




