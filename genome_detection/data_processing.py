
import pandas as pd
import numpy as np
import json

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
#output = open("TCGA_6_Cancer_Type_Mutation_List_sample.csv", "w")


cancer_type_class = data.groupby('Cancer_Type').groups.keys()
Tumor_Sample_ID_class = data.groupby('Tumor_Sample_ID').groups.keys()
Gene_Name_class = data.groupby('Gene_Name').groups.keys()
Chromosome_class = data.groupby('Chromosome').groups.keys()
Variant_Type_class = data.groupby('Variant_Type').groups.keys()
Reference_Allele_class = data.groupby('Reference_Allele').groups.keys()
Tumor_Allele_class = data.groupby('Tumor_Allele').groups.keys()


sample_gene = {}
sample_chrom = {}

sample_variant = {} #sample to gene which has del / ins

len_gen = 20743
len_chrom = 31

from pdb import set_trace
set_trace()

for index, line in data.iterrows():
    write = False
    cancer_index = cancer_type_class.index(line['Cancer_Type'])
    Tumor_Sample_ID_index = Tumor_Sample_ID_class.index(line['Tumor_Sample_ID'])
    Gene_Name_index = Gene_Name_class.index(line['Gene_Name'])
    Chromosome = Chromosome_class.index(line['Chromosome'])
    Variant_type_index = Variant_Type_class.index(line['Variant_Type'])     #0 : INS , 1: DEL
    Reference_Allele_index = Reference_Allele_class.index(line['Reference_Allele'])
    Tumor_Allele_index = Tumor_Allele_class.index(line['Tumor_Allele'])
    
    if Tumor_Sample_ID_index not in sample_gene:
        write = True
        sample_gene[Tumor_Sample_ID_index] = [0.0]*len_gen
        sample_variant[Tumor_Sample_ID_index] = [0.0]*len_gen
   # print(len(sample_gene[Tumor_Sample_ID_index]), Gene_Name_index)
    sample_gene[Tumor_Sample_ID_index][Gene_Name_index] = 1


    if Tumor_Sample_ID_index not in sample_chrom:
        sample_chrom[Tumor_Sample_ID_index] = [0] * len_chrom
    sample_chrom[Tumor_Sample_ID_index][Chromosome] += 1

    ct = line['Cancer_Type']
    var_t = line['Variant_Type']
    Ref = line['Reference_Allele']
    tu_a = line['Tumor_Allele']

    if ct == 'COADREAD':
        if var_t == 'SNP' and 'C' in Ref and 'T' in tu_a:
            sample_variant[Tumor_Sample_ID_index][Gene_Name_index] += 1
            sample_gene[Tumor_Sample_ID_index][Gene_Name_index] += 0.5
    elif ct == 'GBM':
        if var_t == 'SNP' and 'C' in Ref and 'T' in tu_a:
            sample_variant[Tumor_Sample_ID_index][Gene_Name_index] += 1
            sample_gene[Tumor_Sample_ID_index][Gene_Name_index] += 0.5
    elif ct == 'UCEC':
        if var_t == 'SNP' and 'C' in Ref and 'T' in tu_a:
            sample_variant[Tumor_Sample_ID_index][Gene_Name_index] += 1
            sample_gene[Tumor_Sample_ID_index][Gene_Name_index] += 0.5
    elif ct == 'LUAD':
        if var_t == 'SNP' and 'C' in Ref and 'A' in tu_a:
            sample_variant[Tumor_Sample_ID_index][Gene_Name_index] += 1
            sample_gene[Tumor_Sample_ID_index][Gene_Name_index] += 0.5
    elif ct == 'BRCA':
        if var_t == 'DEL' and ('A' in Ref or 'G' in Ref):
            sample_variant[Tumor_Sample_ID_index][Gene_Name_index] += 1
            sample_gene[Tumor_Sample_ID_index][Gene_Name_index] += 0.5



    Start_p = line['Start_Position']
    End_p = line['End_Position']



    tuple_ = str(cancer_index) + "," + str(Tumor_Sample_ID_index)+ "," + str(Start_p) + "," + str(End_p) + "," + str(Variant_type_index) \
            + "," + str(Reference_Allele_index) + "," + str(Tumor_Allele_index) + "\n"

   # if write:
   #     output.write(tuple_)



print("Processing Done.. Trying to Dump")
with open('sample_gene.json', 'w') as f:
    json.dump(sample_gene, f)
with open('sample_chrom.json', 'w') as f:
    json.dump(sample_chrom, f)
with open('sample_variant.json', 'w') as f:
    json.dump(sample_variant, f)

#print(data.groupby('Cancer_Type').var())

