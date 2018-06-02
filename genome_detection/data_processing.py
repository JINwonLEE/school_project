
import pandas as pd





data_list = open("TCGA_6_Cancer_Type_Mutation_List_data.csv", "r")

#divide data
data = open("data_list.csv", "w")
test = open("test_list.csv", "w")
index = 0
for line in data_list:
    index += 1
    if index % 9 == 0:
        test.write(line)
    else:
        data.write(line)



''' # Data Processing for making data.txt
data = pd.read_csv("TCGA_6_Cancer_Type_Mutation_List.csv")

cancer_type_class = data.groupby('Cancer_Type').groups.keys()
Tumor_Sample_ID_class = data.groupby('Tumor_Sample_ID').groups.keys()
Gene_Name_class = data.groupby('Gene_Name').groups.keys()
Variant_Type_class = data.groupby('Variant_Type').groups.keys()
Reference_Allele_class = data.groupby('Reference_Allele').groups.keys()
Tumor_Allele_class = data.groupby('Tumor_Allele').groups.keys()

for index, line in data.iterrows():
    cancer_index = cancer_type_class.index(line['Cancer_Type'])
    Tumor_Sample_ID_index = Tumor_Sample_ID_class.index(line['Tumor_Sample_ID'])
    Gene_Name_index = Gene_Name_class.index(line['Gene_Name'])
    Chromosome = line['Chromosome']
    Start_p = line['Start_Position']
    End_p = line['End_Position']
    Variant_type_index = Variant_Type_class.index(line['Variant_Type'])
    Reference_Allele_index = Reference_Allele_class.index(line['Reference_Allele'])
    Tumor_Allele_index = Tumor_Allele_class.index(line['Tumor_Allele'])

    tuple_ = str(cancer_index) + "," + str(Tumor_Sample_ID_index) + "," + str(Gene_Name_index) + "," + str(Chromosome) + "," + str(Start_p) + "," + str(End_p) + \
            "," + str(Variant_type_index) + "," + str(Reference_Allele_index) + "," + str(Reference_Allele_index) + "," +  str(Tumor_Allele_index) + "\n"

    output.write(tuple_)
'''
#print(data.groupby('Cancer_Type').var())

