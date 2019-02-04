import random
import pandas as pd

fid = pd.read_csv("TCGA_6_Cancer_Type_Mutation_List_indexing.csv", header=None)

fd = fid.sample(frac=1)

fd.to_csv("TCGA_6_Cancer_Type_Mutation_List_shuffle.csv", index=False)

