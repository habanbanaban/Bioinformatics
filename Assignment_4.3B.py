import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("protein_data.csv")

# 23074

plt.scatter([1, 2, 3, 4, 5, 6], data.iloc[1, 1:7], label="Controls")
plt.scatter([1, 2, 3, 4, 5, 6], data.iloc[1, 7:13], label="Patients")
plt.title("Protein 23074 Expression levels")
plt.legend()
plt.show()

# 10994

plt.scatter([1, 2, 3, 4, 5, 6], data.iloc[2, 1:7], label="Controls")
plt.scatter([1, 2, 3, 4, 5, 6], data.iloc[2, 7:13], label="Patients")
plt.title("Protein 10994 Expression levels")
plt.legend()
plt.show()

# Q: Can you see any difference in the distribution between the samples and
# controls for the two proteins?
# A: Yes, the expression levels of protein 23074 appears to be lower in patients than in the control group.
# and the expression levels of protein 10994 seems to be higher in patients than in the control group.
