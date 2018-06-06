import numpy as np
import tensorflow as tf
import os
import csv


<<<<<<< HEAD
INPUT_PATH = "/home/jwl1993/school_project/weather_prediction/"
num_periods = 4
hidden = 6
=======
INPUT_PATH = "/Users/jwl1993/school_project/weather_prediction/"
num_periods = 4
hidden = 6
num_periods = 20        #period that predict output
>>>>>>> 928df1cdbb06263159d9f64e56e96f6dbc5a6bb3
batch_sizes = 10

def load_data():
    train_path = os.path.join(INPUT_PATH, "train_data/train_data_2010-201403")  # Size : 6168
    test_path = os.path.join(INPUT_PATH, "test_data/test_data") # Size : 5520

    train_data_ = None
    test_data_ = None
    with open(train_path, "r") as f:
        reader = csv.reader(f)
        train_data_ = list(reader)

    with open(test_path, "r") as f:
        reader = csv.reader(f)
        test_data_ = list(reader)
    return train_data_, test_data_

train_data, test_data = load_data()
x_test = np.asarray(test_data)
x_test = np.delete(x_test, 0, 1)

x_data = np.asarray(train_data)
x_data = np.delete(x_data, 0, 1) #erase date
index = -1

def next_data(index, batches):
<<<<<<< HEAD
    ret = []
    for i in range(index, index+num_periods):
        ret.append(batches[i][0])
    ret = np.asarray(ret)
    return ret

def next_label(index, batches):
    batch = []
    for b in range(index, index + batch_sizes):
        batch.append(batches[b][0])
    np.asarray(batch)
    return batch
=======
    return batches[index:index+num_periods]
>>>>>>> 928df1cdbb06263159d9f64e56e96f6dbc5a6bb3

#print(len(train_data))
#print(len(train_data) % num_period
#print(x_batches.shape)
#print(x_batches[0])


tf.reset_default_graph()
<<<<<<< HEAD

x = tf.placeholder(tf.float32, [None, num_periods, 1])
y = tf.placeholder(tf.float32, [1])

x_ = tf.reshape(x, [-1,1])
x_ = tf.Print(x_, [x, y])
basic_cell = tf.contrib.rnn.BasicLSTMCell(1, forget_bias=1.0, state_is_tuple=True)
rnn_output, _states = tf.nn.static_rnn(basic_cell,[x_] , dtype=tf.float32)
#rnn_output, states = tf.nn.dynamic_rnn(basic_cell, x, dtype=tf.float32)

#rnn_output = tf.reshape(rnn_output,[1, num_periods])
W = tf.Variable(tf.truncated_normal([1, num_periods], stddev=1))
B = tf.Variable(tf.constant(0.1, shape=[1]))
#output = tf.contrib.layers.fully_connected(rnn_output[, 1, activation_fn=tf.nn.relu)
output = tf.matmul(W,rnn_output[-1]) + B

output = tf.reshape(output, [1])
#outputs = tf.reshape(stacked_output, [1])
#output = tf.Print(output, [output, y])
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=output, labels=y))
train_op = tf.train.AdamOptimizer(1e-3).minimize(cost)
=======
inputs = 1
output = 1

x = tf.placeholder(tf.float32, [None, num_periods, hidden])
y = tf.placeholder(tf.float32, [1])

basic_cell = tf.contrib.rnn.BasicRNNCell(num_units=1)
rnn_output, states = tf.nn.dynamic_rnn(basic_cell, x, dtype=tf.float32)


stacked_rnn_output = tf.reshape(rnn_output, [1])
print(stacked_rnn_output.shape)
#outputs = tf.reshape(stacked_output, [1])

loss = tf.reduce_sum(tf.square(stacked_rnn_output - y))
loss = tf.log(loss)
train_op = tf.train.AdamOptimizer(1e-4).minimize(loss)
>>>>>>> 928df1cdbb06263159d9f64e56e96f6dbc5a6bb3



init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for epochs in range(50):
<<<<<<< HEAD
        for i in range(6000):
            x_batch = next_data(i, x_data)
            x_batch = np.reshape(x_batch, (-1,num_periods,1))
            #y_batch = next_label(i+num_periods, x_data)
            y_batch = x_data[i+num_periods][0]
            y_batch = np.reshape(y_batch, (1))
            sess.run(train_op, feed_dict={x:x_batch, y:y_batch})
            if i % 100 == 0:
                loss_ = cost.eval(feed_dict={x:x_batch, y:y_batch})
                print("Loss in epoch %i iteration %i : %.4f" % (epochs+1, i, loss_))
            '''
=======
        batch_sizes = 10
        for i in range(6000):
            x_batch = next_data(i, x_data)
            y_batch = x_data[i+num_periods+1][0]
            sess.run(train_op, feed_dict={x:x_batch, y:y_batch})
            if i % 100 == 0:
                loss_ = loss.eval(feed_dict={x:x_batch, y:y_batch})
                print("Loss in epoch %i iteration %i : %.4f" % (epochs+1, i, loss_))
                '''
>>>>>>> 928df1cdbb06263159d9f64e56e96f6dbc5a6bb3
        batch_sizes = 48    #528 * 6 = 3168
        print(x_test)
        print("-"*40)
        print(y_test)
        x_ = x.eval(feed_dict={x:x_test, y:y_test})
        o_ = outputs.eval(feed_dict={x:x_test, y:y_test})
        y_ = y.eval(feed_dict={x:x_test, y:y_test})
        print("x data : %.4f" %x_[0,0,0])
        print("output data : %.4f" %o_[0,0,0])
        print("y data : %.4f" %y_[0,0,0])
        acc = loss.eval(feed_dict={x:x_test, y:y_test})
        print("Loss in epoch %i : %.4f " % (epochs+1, acc))


    print("Optimized Done")
    start_point = 0
    batch_sizes = 48    #528 * 6 = 3168
    x_test = next_data(0, True, x_test_batches)
    y_test = next_data(1, False, x_test_batches)
    x_ = x.eval(feed_dict={x:x_test, y:y_test})
    o_ = outputs.eval(feed_dict={x:x_test, y:y_test})
    y_ = y.eval(feed_dict={x:x_test, y:y_test})
    print("x data : %.4f" %x_[0,0,1])
    print("output data : %.4f" %o_[0,0,1])
    print("y data : %.4f" %y_[0,0,1])
    acc = loss.eval(feed_dict={x:x_test, y:y_test})
    print("Loss in total : %.4f " % acc)

'''


