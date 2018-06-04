import pandas as pd
import tensorflow as tf
import numpy 

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical

whole_data = numpy.loadtxt("TCGA_6_Cancer_Type_Mutation_List_data.csv", delimiter=",")

columns = 5
out_columns = 7

model = Sequential()
X = whole_data[:,2:7]
Y = to_categorical(whole_data[:,0])
model.add(Dense(128, input_dim=columns, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(out_columns, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X, Y, validation_split=0.2, epochs=9, batch_size=32)
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))



