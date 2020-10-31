from random import choice

length = int(input("How many nucleotides should the DNA sequence contain? "))
random_dna = ''
for i in range(length):
    random_nn = choice(['A', 'T', 'C', 'G'])
    random_dna = random_dna + random_nn

x = len(random_dna)
gc = random_dna.count('G') + random_dna.count('C')
gc_content = gc / x * 100

print(random_dna)
print(f"The sequence contains {len(random_dna)} nucleotides")
print(f"The gc content is {gc_content}")
