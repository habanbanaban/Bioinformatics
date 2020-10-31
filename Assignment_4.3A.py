import pandas as pd
import numpy as np

lst = []
data = pd.read_csv("protein_data.csv")
controls = ["C1", "C2", "C3", "C4", "C5", "C6"]
patients = ["P1", "P2", "P3", "P4", "P5", "P6"]
for index, row in data.iterrows():
    lst2 = [row[0], row[controls].mean(), row[controls].std(), row[patients].mean(), row[patients].std()]
    lst.append(lst2)

df = pd.DataFrame(lst, columns=["protein ID", "Control mean", "Control stdev", "Patient mean", "Patient stdev"])
df.to_csv("Assignment4.3A.csv", sep="\t", index=False)
