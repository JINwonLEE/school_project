'''
Data Processing

----------INTPUT-----------

csv file which has data as :
    Cancer Type, Tumor Sample ID, Gene Name, Chromosome, Start Position, End Position, Variant Type, Reference Allele, Tumor Allele

----------OUTPUT-----------

It will be changed into format as :
    Cancer Type, Tumor Sample ID

And there will be two dumped file with json :

    sample_gene : It is dictionary which Tumor Sample ID is the key and the value will be the gene list
                  which is in the Tumor Sample ID

    sample_variant : It is dictionary which Tumor Sample ID is the key and the value will be the gene list
                     which is critical to cancer occurance
'''

import pandas as pd
import numpy as np
import json

from sklearn.model_selection import train_test_split


GENE_LENGTH = 20743

data = pd.read_csv("TCGA_6_Cancer_Type_Mutation_List.csv")

output = open("TCGA_6_Cancer_Type_Mutation_List_indexing.csv", "w")    # Output file : cancer type, sample id


cancer_type_class = data.groupby('Cancer_Type').groups.keys()
tum_s_id = data.groupby('Tumor_Sample_ID').groups.keys()
gene_name = data.groupby('Gene_Name').groups.keys()
variant_type = data.groupby('Variant_Type').groups.keys()
ref_allele = data.groupby('Reference_Allele').groups.keys()
tumor_allele = data.groupby('Tumor_Allele').groups.keys()


sample_gene = {}

sample_variant = {} #sample to gene which has variant type DEL or INS


for index, line in data.iterrows():
    write = False
    cancer_index = cancer_type_class.index(line['Cancer_Type'])
    tum_id_ind = tum_s_id.index(line['Tumor_Sample_ID'])
    gene_ind = gene_name.index(line['Gene_Name'])
    variant_ind = variant_type.index(line['Variant_Type'])
    ref_allele_ind = ref_allele.index(line['Reference_Allele'])
    tumor_allele_ind = tumor_allele.index(line['Tumor_Allele'])

    if tum_id_ind not in sample_gene:           # If there is no index in sample_gene, sample_variant dictionary, make list with length GENE_LENGTH  
        write = True                            # If write is true it will write the sample id and cancer type that the sample has in output file
        sample_gene[tum_id_ind] = [0.0] * GENE_LENGTH
        sample_variant[tum_id_ind] = [0.0] * GENE_LENGTH

    sample_gene[tum_id_ind][gene_ind] = 1

    ct = line['Cancer_Type']
    var_t = line['Variant_Type']
    Ref = line['Reference_Allele']
    tu_a = line['Tumor_Allele']

    # Check the special cases which some variant affects certain cancer occurence 
    if ct == 'COADREAD':
        if var_t == 'SNP' and 'C' in Ref and 'T' in tu_a:
            sample_variant[tum_id_ind][gene_ind] += 1
            sample_gene[tum_id_ind][gene_ind] += 0.5
    elif ct == 'GBM':
        if var_t == 'SNP' and 'C' in Ref and 'T' in tu_a:
            sample_variant[tum_id_ind][gene_ind] += 1
            sample_gene[tum_id_ind][gene_ind] += 0.5
    elif ct == 'UCEC':
        if var_t == 'SNP' and 'C' in Ref and 'T' in tu_a:
            sample_variant[tum_id_ind][gene_ind] += 1
            sample_gene[tum_id_ind][gene_ind] += 0.5
    elif ct == 'LUAD':
        if var_t == 'SNP' and 'C' in Ref and 'A' in tu_a:
            sample_variant[tum_id_ind][gene_ind] += 1
            sample_gene[tum_id_ind][gene_ind] += 0.5
    elif ct == 'BRCA':
        if var_t == 'DEL' and ('A' in Ref or 'G' in Ref):
            sample_variant[tum_id_ind][gene_ind] += 1
            sample_gene[tum_id_ind][gene_ind] += 0.5

    if write:
        tuple_ = str(cancer_index) + "," + str(tum_id_ind) + "\n"
        output.write(tuple_)

print("Processing Done.. Trying to Dump")
with open('sample_gene.json', 'w') as f:
    json.dump(sample_gene, f)
with open('sample_variant.json', 'w') as f:
    json.dump(sample_variant, f)


