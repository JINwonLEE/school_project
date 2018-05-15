import numpy as np
import tensorflow as tf
import os
import csv


INPUT_PATH = "/home/jwl1993/school_project/weather_prediction/"
num_periods = 200
hidden = 6
start_point = 0

def load_data():
    train_path = os.path.join(INPUT_PATH, "train_data/normalized_train_data.txt")
    test_path = os.path.join(INPUT_PATH, "test_data/normalized_test_data.txt")

    train_data_ = None
    test_data_ = None
    with open(train_path, "r") as f:
        reader = csv.reader(f)
        train_data_ = list(reader)

    with open(test_path, "r") as f:
        reader = csv.reader(f)
        test_data_ = list(reader)
    return train_data_, test_data_

num_periods = 20        #period that predict output
batch_sizes = 10
train_data, test_data = load_data()
x_test = np.asarray(test_data)
x_test = np.delete(x_test, 0, 1)
x_test_batches = x_test.reshape(-1, batch_sizes, hidden)

x_data = np.asarray(train_data)
x_data = np.delete(x_data, 0, 1) #erase date
x_batches = x_data.reshape(-1,batch_sizes, hidden)
index = -1

def next_data(index, check, st, batches):
    if check:
        st += 1
    return batches[st + index: st + index+num_periods]

#print(len(train_data))
#print(len(train_data) % num_period
#print(x_batches.shape)
#print(x_batches[0])


tf.reset_default_graph()
inputs = 1
output = 1

x = tf.placeholder(tf.float32, [num_periods, batch_sizes, hidden])
y = tf.placeholder(tf.float32, [num_periods, batch_sizes, hidden])

basic_cell = tf.contrib.rnn.BasicRNNCell(num_units=hidden, activation=tf.nn.relu)
rnn_output, states = tf.nn.dynamic_rnn(basic_cell, x, dtype=tf.float32)

learning_rate = 0.0001

stacked_rnn_output = tf.reshape(rnn_output, [-1,hidden])
stacked_output = tf.layers.dense(stacked_rnn_output, hidden)
#print(stacked_rnn_output.shape)
outputs = tf.reshape(stacked_output, [num_periods,batch_sizes, hidden])

loss = tf.reduce_sum(tf.square(outputs - y))
train_op = tf.train.AdamOptimizer(2e-4).minimize(loss)



init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for epochs in range(5):
        batch_sizes = 10
        for i in range(5500):
            x_batch = next_data(i, True, start_point, x_batches)
            y_batch = next_data(i+1, False, start_point, x_batches)
            sess.run(train_op, feed_dict={x:x_batch, y:y_batch})
            if i % 100 == 0:
                loss_ = loss.eval(feed_dict={x:x_batch, y:y_batch})
                print("Loss in epoch %i iteration %i : %.4f" % (epochs+1, i, loss_))
        batch_sizes = 48    #528 * 6 = 3168
        x_test = next_data(0, True, start_point, x_test_batches)
        y_test = next_data(1, False, start_point, x_test_batches)
        x_ = x.eval(feed_dict={x:x_test, y:y_test})
        o_ = outputs.eval(feed_dict={x:x_test, y:y_test})
        y_ = y.eval(feed_dict={x:x_test, y:y_test})
        print("x data : %.4f" %x_[0,0,1])
        print("output data : %.4f" %o_[0,0,1])
        print("y data : %.4f" %y_[0,0,1])
        acc = loss.eval(feed_dict={x:x_test, y:y_test})
        print("Loss in epoch %i : %.4f " % (epochs+1, acc))


    print("Optimized Done")
    start_point = 0
    batch_sizes = 48    #528 * 6 = 3168
    x_test = next_data(0, True, start_point, x_test_batches)
    y_test = next_data(1, False, start_point, x_test_batches)
    x_ = x.eval(feed_dict={x:x_test, y:y_test})
    o_ = outputs.eval(feed_dict={x:x_test, y:y_test})
    y_ = y.eval(feed_dict={x:x_test, y:y_test})
    print("x data : %.4f" %x_[0,0,1])
    print("output data : %.4f" %o_[0,0,1])
    print("y data : %.4f" %y_[0,0,1])
    acc = loss.eval(feed_dict={x:x_test, y:y_test})
    print("Loss in total : %.4f " % acc)




