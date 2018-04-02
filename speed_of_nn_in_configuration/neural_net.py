import tensorflow as tf
import time
import os

training_epochs = 10000

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "/dataset/data.txt"


input_ = tf.placeholder(tf.float32, shape=[1,4], name='configuration')
output_ = tf.placeholder(tf.float32, name='speed')

with tf.name_scope('weights'):
    W1 = tf.Variable(tf.truncated_normal(shape=[4, 500], stddev=1.0))
    W2 = tf.Variable(tf.truncated_normal(shape=[500, 100], stddev=1.0))
    W3 = tf.Variable(tf.truncated_normal(shape=[100, 10], stddev=1.0))
    W4 = tf.Variable(tf.truncated_normal(shape=[10, 1], stddev=1.0))

with tf.name_scope('biases'):
    biases1 = tf.constant(1.1, shape=[1,500])
    biases2 = tf.constant(1.1, shape=[1,100])
    biases3 = tf.constant(1.1, shape=[1,10])
    biases4 = tf.constant(1.1, shape=[1])

    tf.Variable(biases1)
    tf.Variable(biases2)
    tf.Variable(biases3)
    tf.Variable(biases4)


layer_1 = tf.nn.relu(tf.add(tf.matmul(input_, W1), biases1))
layer_2 = tf.nn.relu(tf.add(tf.matmul(layer_1, W2), biases2))
layer_3 = tf.nn.relu(tf.add(tf.matmul(layer_2, W3), biases3))
layer_4 = tf.add(tf.matmul(layer_3, W4), biases4)

acc = tf.subtract(layer_4, output_)

loss = tf.pow(acc, tf.constant(value=2.0, shape=[1]))

loss = tf.reduce_mean(loss)

train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)


#print_test = tf.Print(total, [input_, output_], name='printer')


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    index = 0
    with open(filename) as inp:
        data_ = inp.readlines()
        for i in range(training_epochs):
            for line in data_:
                line = line.strip().split(", ")
                n_ps, n_worker, batch_size, n_gpu = line[0].strip().split(",")
                n_ps = (float)(n_ps[-1])
                n_gpu = (float)(n_gpu[0])
                n_worker = (float)(n_worker)
                batch_size = (float)(batch_size)
                speed = (float)(line[1][1:-2])
                test = sess.run([train_step, loss] , feed_dict={input_:[[n_ps, n_worker, batch_size, n_gpu]], output_:speed})
                if index % 100 == 0:
                    accuracy = sess.run([acc], feed_dict={input_:[[n_ps, n_worker, batch_size, n_gpu]], output_:speed})
                    print(accuracy)

                index += 1

