from Bio import SeqIO
sequenceList = []
for seq_record in SeqIO.parse("Genes.fa", "fasta"):
    if len(seq_record.seq) < 200:
        None
    else:
        sequenceList.append(seq_record)

with open("Assignment4.1.fa", "w") as outfile:
    for element in sequenceList:
        if "*" in element.translate().seq:
            outfile.write(element.description + "\n")
            outfile.write(str(element.translate().seq.split("*")[0]) + "\n")
        else:
            outfile.write(element.description + "\n")
            outfile.write(str(element.translate().seq) + "\n")
