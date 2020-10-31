
aminoacids = {
    'gga': 'G',
    'ggc': 'G',
    'ggg': 'G',
    'ggt': 'G',
    'gca': 'A',
    'gcc': 'A',
    'gcg': 'A',
    'gct': 'A',
    'gta': 'V',
    'gtc': 'V',
    'gtg': 'V',
    'gtt': 'V',
    'tta': 'L',
    'ttg': 'L',
    'cta': 'L',
    'ctc': 'L',
    'ctg': 'L',
    'ctt': 'L',
    'ata': 'I',
    'atc': 'I',
    'att': 'I',
    'atg': 'M',
    'cca': 'P',
    'ccc': 'P',
    'ccg': 'P',
    'cct': 'P',
    'ttc': 'F',
    'ttt': 'F',
    'tgg': 'W',
    'agc': 'S',
    'agt': 'S',
    'tca': 'S',
    'tcc': 'S',
    'tcg': 'S',
    'tct': 'S',
    'aca': 'T',
    'acc': 'T',
    'acg': 'T',
    'act': 'T',
    'caa': 'Q',
    'cag': 'Q',
    'tac': 'Y',
    'tat': 'Y',
    'tgc': 'C',
    'tgt': 'C',
    'aaa': 'K',
    'aag': 'K',
    'aga': 'R',
    'agg': 'R',
    'cga': 'R',
    'cgc': 'R',
    'cgg': 'R',
    'cgt': 'R',
    'cac': 'H',
    'cat': 'H',
    'gac': 'D',
    'gat': 'D',
    'gaa': 'E',
    'gag': 'E',
    'tag': 'STOP',
    'taa':'STOP',
    'uga':'STOP',


}


class DNA:
    def __init__(self, sequence):
        if not sequence.startswith("atg"):
            raise Exception("Invalid Protein Coding Unit, ATG missing")
        self.sequence = sequence.lower()
        self.sequence = self.sequence.replace("u", "t")

        self.aminoacids = self.get_aminoacids(self.sequence)

    def get_aminoacids(self, seq):

        acids = []

        while len(seq) >= 3:
            aa = seq[:3]
            if aa in aminoacids:
                acids.append(aminoacids[aa])
            else:
                print("Invalid codon")
            if 'STOP' in acids:
                return acids
            seq = seq[3:]

        return acids

userinput = input("Enter DNA sequence: ").strip()
DNA1 = DNA(sequence=userinput)

userinput2 = input("Enter another DNA sequence: ").strip()
DNA2 = DNA(sequence=userinput2)

if DNA1.sequence == DNA2.sequence :
    print("No mutation found in DNA sequence")
    print(DNA1.aminoacids)

elif DNA1.aminoacids == DNA2.aminoacids:
    print("Silent mutation found in DNA sequence")
    print(DNA1.aminoacids)

else:
    print("Amino acid mutation detected")
    print(DNA1.aminoacids)
    print(DNA2.aminoacids)
