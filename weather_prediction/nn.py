
import sys
import random
import numpy as np
#import pylab
import datetime
#import matplotlib.pyplot as plt

from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential


INPUT_DIM = 5
OUTPUT_DIM = 1
EPOCHS = 10
load_model_ = False
#load_model_ = True
#test_model_ = False
test_model_ = True

h5_name=""

def log(func):
    def print_msg(msg):
        print("[%s]" % datetime.datetime.now(), msg)
        return func
    return print_msg

#@log("build_model")
def build_model(learning_rate=0.05):
    model = Sequential()
    model.add(Dense(30, input_dim=INPUT_DIM, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(30, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(30, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(30, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(OUTPUT_DIM, activation='linear', kernel_initializer='he_uniform'))
    model.summary()
    model.compile(loss='mse', optimizer=Adam(lr=learning_rate))
    return model


#@log("train_model")
def train_model(model, data):
    x_data = data[:,2:]
    y_data = data[:,1]
    hist = model.fit(x_data, y_data, epochs=EPOCHS)
    model.save_weights('./nn.h5')
    return hist 

#@log("test_model")
def test_model(model, data):
    x_data = data[:,2:]
    real_values = data[:,1]
    diff = []
    for i,j in zip(x_data, real_values):
        y_predict = model.predict(np.reshape(i,(1,5)))
        diff.append(abs(y_predict-j))
        #print(y_predict[0])
    #print("sum = %d, len = %d" %(sum(diff),len(diff)))
    return float(sum(diff))/float(len(diff))

def func(x):
    if x == '':
        return 0
    else:
        return float(x)

#@log("read_file")
def readFile(inFile):
    data = []
    while True:
        line = inFile.readline().strip()
        if not line:
            break
        line = line.split(',')
        line = list(map(func, line))

        data.append(line)

    return data 


if __name__ == "__main__":
    if len(sys.argv) > 3:
        trainFile = open(sys.argv[1], 'r')
        testFile = open(sys.argv[2], 'r')
        h5_name = sys.argv[3]

    elif len(sys.argv) > 2:
        trainFile = open(sys.argv[1], 'r')
        testFile = open(sys.argv[2], 'r')
        h5_name = "nn.h5"
        outFile = sys.stdout
    else:
        print("Argument Error.")
        exit(0)

    #print(np.shape(Data[:,2:]))
    model = build_model()
    if not load_model_:
        train_data = np.array(readFile(trainFile))
        hist = train_model(model, train_data)
    else:
        #model.load_weights('./nn.h5')
        model.load_weights(h5_name)
    
    
    if test_model_:
        print("-"*40)
        print("Testing..")
        test_data = np.array(readFile(testFile))
        accuracy = test_model(model, test_data)
        print("Average Temperature difference : %f " % accuracy )

    #y_predict = model.predict(np.array([1,2,3,4]))
    #print(y_predict[0])
    print(hist.history['loss'])
    sys.exit()
    """
    plt.plot(hist.history['loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    #plt.show()
    """ 

