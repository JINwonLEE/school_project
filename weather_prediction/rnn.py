
import sys
import random
import numpy as np
#import pylab
import datetime
#import matplotlib.pyplot as plt
#%matplotlib inline

from keras.layers import SimpleRNN, Dense
from keras.optimizers import Adam
from keras.models import Sequential



INPUT_DIM = 10
OUTPUT_DIM = 4
EPOCHS = 5
load_model_ = False
#load_model_ = True
#test_model_ = False
test_model_ = True



def seq2dataset(seq, window_size):
    dataset = []
    for i in range(len(seq)-window_size):
        subset = seq[i:(i+window_size+1)]
        dataset.append(subset)
    return np.array(dataset)


def build_model(learning_rate=0.05):
    model = Sequential()
    #model.add(SimpleRNN(10, input_shape=(INPUT_DIM,1)))
    #model.add(Dense(1, activation='linear', kernel_initializer='he_uniform'))
    model.add(Dense(128, input_dim=INPUT_DIM, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(OUTPUT_DIM, activation='linear', kernel_initializer='he_uniform'))

    model.summary()
    model.compile(loss='mse', optimizer=Adam(lr=learning_rate))
    return model


def train_model(model, data):
    x_data = data[:,0:INPUT_DIM]
    y_data = data[:,INPUT_DIM:]
    print(np.shape(data))
    print(np.shape(x_data))
    print(np.shape(y_data))
    hist = model.fit(x_data, y_data, epochs=EPOCHS)
    model.save_weights('./rnn.h5')
    return hist 

def test_model(model, data):
    x_data = data[:,0:INPUT_DIM]
    real_values = data[:,INPUT_DIM:]
    diff = []
    for i,j in zip(x_data, real_values):
        y_predict = model.predict(np.reshape(i,(1,INPUT_DIM)))
        difference = abs(y_predict-j)[0]
        for axis in range(OUTPUT_DIM):
            diff.append(difference[axis])
            #print(difference[axis])
        #diff.append(abs(y_predict-j))
    #print("sum = %d, len = %d" %(sum(diff),len(diff)))
    return float(sum(diff))/float(len(diff))

def func(x):
    if x == '':
        return 0
    else:
        return float(x)


def readFile(inFile):
    seq = []
    while True:
        line = inFile.readline().strip()
        if not line:
            break
        line = line.split(',')
        line = list(map(func, line))
        seq.append(line[1])

    return seq


if __name__ == "__main__":
    if len(sys.argv) > 3:
        trainFile = open(sys.argv[1], 'r')
        testFile = open(sys.argv[2], 'r')
        h5_name = sys.argv[3]
    elif len(sys.argv) > 2:
        trainFile = open(sys.argv[1], 'r')
        testFile = open(sys.argv[2], 'r')
        h5_name = "rnn.h5"
        outFile = sys.stdout
    else:
        print("Argument Error.")
        exit(0)

    model = build_model()
    if not load_model_:
        seq_data = readFile(trainFile)
        #dataset = seq2dataset(seq_data, window_size=4)
        dataset = seq2dataset(seq_data, window_size=INPUT_DIM+OUTPUT_DIM-1)
        print(dataset)
        print("-"*40)
        hist = train_model(model, dataset)
    else:
        #model.load_weights('./rnn.h5')
        model.load_weights(h5_name)
    
    if test_model_:
        test_seq_data = readFile(testFile)
        #dataset = seq2dataset(test_seq_data, window_size=4)
        dataset = seq2dataset(test_seq_data, window_size=INPUT_DIM+OUTPUT_DIM-1)
        accuracy = test_model(model, dataset)
        print("Average Temperature difference : %f " % accuracy )

    #print(hist.history['loss'])
    pred_val = model.predict(np.reshape(np.array([23.9, 22, 22, 26, 23 , 22, 20, 21, 15,
        13]), (1,10)))
    print(pred_val)
    trainFile.close()
    testFile.close()
    sys.exit()
    """
    plt.plot(hist.history['loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    #plt.show()
    """ 

