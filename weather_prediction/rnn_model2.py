import numpy as np
import tensorflow as tf
import os
import csv


INPUT_PATH = "/Users/jwl1993/school_project/weather_prediction/"
num_periods = 200
hidden = 6

def load_data():
    train_path = os.path.join(INPUT_PATH, "train_data/normalized_train_data.txt")
    test_path = os.path.join(INPUT_PATH, "test_data/test_data")

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
#x_test = np.asarray(test_data)
#x_test = np.delete(x_test, 0, 1)
#x_test_batches = x_test.reshape(-1, batch_sizes, 6)

x_data = np.asarray(train_data)
x_data = np.delete(x_data, 0, 1) #erase date
x_batches = x_data.reshape(-1,batch_sizes, hidden)
index = -1

def next_data(index):
    return x_batches[index:index+num_periods]

print(len(train_data))
print(len(train_data) % num_periods)
print(x_batches.shape)
print(x_batches[0])


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
train_op = tf.train.AdamOptimizer(1e-4).minimize(loss)



init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for epochs in range(50):
        for i in range(5500):
            x_batch = next_data(i)
            y_batch = next_data(i+1)
            sess.run(train_op, feed_dict={x:x_batch, y:y_batch})
            loss_ = loss.eval(feed_dict={x:x_batch, y:y_batch})
            print("Loss in iteration %i : %.4f" % (i, loss_))





