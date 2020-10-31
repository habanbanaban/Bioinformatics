n = 0
sequence_list = []
while n < 4:
    sequence = input("Enter DNA sequence: ")
    sequence_list.append(sequence)
    n += 1
m = 0
while m < 4:
    print("sequence:", sequence_list[m], ",", "length of sequence:", len(sequence_list[m]))
    m += 1