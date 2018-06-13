import pandas as pd
import tensorflow as tf
import numpy 
import json

from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Input, concatenate
from keras.utils import to_categorical




'''
You should make json 3 json files sample_gene, sample_chrom, sample_variant
'''


whole_data = numpy.loadtxt("TCGA_6_Cancer_Type_Mutation_List_sample2.csv", delimiter=",")

columns = 3
out_columns = 7
len_gen = 20743
len_chrom = 31

sample_gene = None
sample_chrom = None
sample_variant = None
with open('sample_gene.json', 'r') as f:
    sample_gene = json.load(f)

with open('sample_chrom.json', 'r') as f:
    sample_chrom = json.load(f)

with open('sample_variant.json', 'r') as f:
    sample_variant = json.load(f)

tmp = whole_data[:,1]

x_list = []
x2_list = []
x3_list = []

for i in tmp:
    x2_list.append(sample_chrom[str(int(i))])
x2_list = numpy.array(x2_list)

for i in tmp:
    x_list.append(sample_gene[str(int(i))])

x_list = numpy.array(x_list)


for i in tmp:
    x3_list.append(sample_variant[str(int(i))])

x3_list = numpy.array(x3_list)
#x3_list = whole_data[:,4:7]

print("Neural Net Start")

Y = to_categorical(whole_data[:,0], num_classes=out_columns)

inputs = Input(shape=(len_gen,))
inputs2 = Input(shape=(len_chrom,))
inputs3 = Input(shape=(len_gen,))


lay3_1 = Dense(64, activation='relu')(inputs3)
lay3_3 = Dense(32, activation='relu')(lay3_1)


#lay2_1 = Dense(64, activation='relu')(inputs2)
#lay2_3 = Dense(32, activation='relu')(lay2_1)


lay1_1 = Dense(64, activation='relu')(inputs)
#lay4 = concatenate([lay1_1, lay2_3, lay3_3])
lay4 = concatenate([lay1_1, lay3_3])
lay6 = Dense(16, activation='relu')(lay4)
lay7 = Dense(out_columns, activation='softmax')(lay6)

#model = Model(inputs=[inputs,inputs2, inputs3], outputs=lay7)
model = Model(inputs=[inputs, inputs3], outputs=lay7)
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
#model.fit([x_list, x2_list, x3_list],Y, epochs=30, validation_split=0.2, batch_size=32)
model.fit([x_list, x3_list],Y, epochs=20, validation_split=0.2, batch_size=8)


#scores = model.evaluate([x_list, x2_list, x3_list], Y)
scores = model.evaluate([x_list, x3_list], Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


'''
model = Sequential()
#X = whole_data[:,1:9]
X = x_list[]
Y = to_categorical(whole_data[:,0], num_classes=out_columns)
model.add(Dense(128, input_dim=len_gen, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(out_columns, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X, Y, epochs=10, batch_size=128)
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
'''
