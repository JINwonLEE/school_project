
import pandas as pd
import numpy as np


from sklearn.model_selection import train_test_split
'''
data_list = pd.read_csv("TCGA_6_Cancer_Type_Mutation_List_data.csv")
train, test = train_test_split(data_list, test_size=0.15)
train.to_csv("data_list.csv", index=False)
test.to_csv("test_list.csv", index=False)

#divide data
'''

 # Data Processing for making data.txt
data = pd.read_csv("TCGA_6_Cancer_Type_Mutation_List.csv")
output = open("TCGA_6_Cancer_Type_Mutation_List_data.csv", "w")

cancer_type_class = data.groupby('Cancer_Type').groups.keys()
Tumor_Sample_ID_class = data.groupby('Tumor_Sample_ID').groups.keys()
Gene_Name_class = data.groupby('Gene_Name').groups.keys()
Chromosome_class = data.groupby('Chromosome').groups.keys()
Variant_Type_class = data.groupby('Variant_Type').groups.keys()
Reference_Allele_class = data.groupby('Reference_Allele').groups.keys()
Tumor_Allele_class = data.groupby('Tumor_Allele').groups.keys()

for index, line in data.iterrows():
    cancer_index = cancer_type_class.index(line['Cancer_Type'])
    Tumor_Sample_ID_index = Tumor_Sample_ID_class.index(line['Tumor_Sample_ID'])
    Gene_Name_index = Gene_Name_class.index(line['Gene_Name'])
    Chromosome = Chromosome_class.index(line['Chromosome'])
    Start_p = line['Start_Position']
    End_p = line['End_Position']
    Variant_type_index = Variant_Type_class.index(line['Variant_Type'])
    Reference_Allele_index = Reference_Allele_class.index(line['Reference_Allele'])
    Tumor_Allele_index = Tumor_Allele_class.index(line['Tumor_Allele'])

    tuple_ = str(cancer_index) + "," + str(Tumor_Sample_ID_index) + "," + str(Gene_Name_index) + "," + str(Chromosome) + "," + str(Start_p) + "," + str(End_p) + \
            "," + str(Variant_type_index) + "," + str(Reference_Allele_index) + "," +  str(Tumor_Allele_index) + "\n"

    output.write(tuple_)

#print(data.groupby('Cancer_Type').var())

