import pandas as pd

data = pd.read_csv("data_list.csv")
test = pd.read_csv("test_list.csv")

r = data.iterrows()

#Return is_data_finish, batch_input
def get_next_data(batch):
    index = 0
    input_ = []
    for _, row in r:
        index += 1

        input_.append([row['Cancer_Type'], row['Tumor_Sample_ID'], row['Gene_Name'], \
                row['Chromosome'], row['Start_Position'], row['End_Position'], row['Variant_Type'], \
                row['Reference_Allele'], row['Tumor_Allele']])

        if index == batch:
            return False, input_
    return True, input_


print(get_next_data(3))
print(get_next_data(3))


