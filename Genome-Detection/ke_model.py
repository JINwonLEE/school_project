'''
Neural net model with Keras

Training neural net model with shuffled data set
Neural net has two inputs and one output and neural network is like below :

      Input1            Input2
    (sample_gene)   (sample_variant)
        |               |
    FC layer         FC layer
        |               |
        |            FC layer
        |              /
        |             /
        Concatenation
              |
           FC layer
              |
           FC layer
              |
           Output (Cancer Type)

'''
import numpy
import json

from keras.models import Model
from keras.layers import Dense, Input, concatenate
from keras.utils import to_categorical

'''
You should make json 2 json files sample_gene, sample_variant
'''

whole_data = numpy.loadtxt("TCGA_6_Cancer_Type_Mutation_List_shuffle_data.csv", delimiter=",")

CANCER_TYPE_LENGTH = 7
GENE_LENGTH = 20743

sample_gene = None
sample_variant = None

with open('sample_gene.json', 'r') as f:
    sample_gene = json.load(f)

with open('sample_variant.json', 'r') as f:
    sample_variant = json.load(f)

tum_s_id = whole_data[:,1]

gene_list = []
variant_list = []

for i in tum_s_id:
    gene_list.append(sample_gene[str(int(i))])

gene_list = numpy.array(gene_list)

for i in tum_s_id:
    variant_list.append(sample_variant[str(int(i))])

variant_list = numpy.array(variant_list)

print("Neural Net Generation")

Y = to_categorical(whole_data[:,0], num_classes=CANCER_TYPE_LENGTH)

input1 = Input(shape=(GENE_LENGTH,))
input2 = Input(shape=(GENE_LENGTH,))

lay2_1 = Dense(64, activation='relu')(input2)
lay2_2 = Dense(32, activation='relu')(lay2_1)

lay1_1 = Dense(64, activation='relu')(input1)
lay3 = concatenate([lay1_1, lay2_2])
lay4 = Dense(16, activation='relu')(lay3)
lay5 = Dense(CANCER_TYPE_LENGTH, activation='softmax')(lay4)

model = Model(inputs=[input1, input2], outputs=lay5)
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit([gene_list, variant_list],Y, epochs=20, validation_split=0.2, batch_size=8)

scores = model.evaluate([gene_list, variant_list], Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

