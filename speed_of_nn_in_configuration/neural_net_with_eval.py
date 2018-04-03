import tensorflow as tf
import time
import os
import sys

training_epochs = 10000

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "/dataset/data.txt"
eval_filename = dir_path + "/dataset/test.txt"

test_filename = dir_path + "/dataset/test.txt"

model_path = sys.argv[2]

input_ = tf.placeholder(tf.float32, shape=[1,4], name='configuration')
output_ = tf.placeholder(tf.float32, name='speed')

with tf.name_scope('weights'):
    W1 = tf.Variable(tf.truncated_normal(shape=[4, 500], stddev=1.0))
    W2 = tf.Variable(tf.truncated_normal(shape=[500, 100], stddev=1.0))
    W3 = tf.Variable(tf.truncated_normal(shape=[100, 10], stddev=1.0))
    W4 = tf.Variable(tf.truncated_normal(shape=[10, 5], stddev=1.0))
    W5 = tf.Variable(tf.truncated_normal(shape=[5, 1], stddev=1.0))

with tf.name_scope('biases'):
    biases1 = tf.constant(1.2, shape=[1,500])
    biases2 = tf.constant(1.2, shape=[1,100])
    biases3 = tf.constant(1.2, shape=[1,10])
    biases4 = tf.constant(1.2, shape=[5])
    biases5 = tf.constant(1.2, shape=[1])

    tf.Variable(biases1)
    tf.Variable(biases2)
    tf.Variable(biases3)
    tf.Variable(biases4)
    tf.Variable(biases5)


layer_1 = tf.nn.tanh(tf.add(tf.matmul(input_, W1), biases1))
layer_2 = tf.nn.tanh(tf.add(tf.matmul(layer_1, W2), biases2))
#layer_3 = tf.nn.tanh(tf.contrib.layers.batch_norm(tf.add(tf.matmul(layer_2, W3), biases3), center=True, scale=True, is_training=True, scope='bn'))
layer_3 = tf.nn.relu(tf.add(tf.matmul(layer_2, W3), biases3))
layer_4 = tf.nn.relu(tf.add(tf.matmul(layer_3, W4), biases4))
layer_5 = tf.add(tf.matmul(layer_4, W5), biases5)
#layer_5 = tf.Print(layer_5, [layer_5],message="this is layer 5 output : ")


acc = tf.subtract(layer_5, output_)

acc_sum = tf.reduce_sum(acc)
#acc_sum = tf.Print(acc_sum, [acc_sum], message="acc_sum : ")

loss = tf.pow(acc, tf.constant(value=2.0, shape=[1]))

loss = tf.reduce_mean(loss)

train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)

saver = tf.train.Saver()
#print_test = tf.Print(total, [input_, output_], name='printer')


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    index = 0
    if sys.argv[1] == 'eval' :
        saver.restore(sess, model_path)
        with open(eval_filename) as inp:
            data_ = inp.readlines()
            for line in data_:
                line = line.strip().split(", ")
                n_ps, n_worker, batch_size, n_gpu = line[0].strip().split(",")
                n_ps = (float)(n_ps[-1])
                n_gpu = (float)(n_gpu[0])
                n_worker = (float)(n_worker)
                batch_size = (float)(batch_size)
                speed = []
                speed.append((float)(line[1][1:-2]))
                eval_val = sess.run([layer_5], feed_dict={input_:[[n_ps, n_worker, batch_size, n_gpu]], output_:speed})
                print("%s  %.3f" % (line, eval_val[0]))
    else :
        for i in range(training_epochs):
            with open(filename) as inp:
                data_ = inp.readlines()
                for line in data_:
                    line = line.strip().split(", ")
                    n_ps, n_worker, batch_size, n_gpu = line[0].strip().split(",")
                    n_ps = (float)(n_ps[-1])
                    n_gpu = (float)(n_gpu[0])
                    n_worker = (float)(n_worker)
                    batch_size = (float)(batch_size)
                    speed = []
                    speed.append((float)(line[1][1:-2]))
            #	print(speed)
                    test = sess.run([train_step, loss] , feed_dict={input_:[[n_ps, n_worker, batch_size, n_gpu]], output_:speed})
                    if index % 1000 == 0:
                        num_test_data = 40.0
                        difference = 0.0
                        with open(test_filename) as tes:
                            test_data = tes.readlines()
                            for l in test_data:
                               # print(l)
                                tline = l.strip().split(", ")
                                tn_ps, tn_worker, tbatch_size, tn_gpu = tline[0].strip().split(",")
                                tn_ps = (float)(tn_ps[-1])
                                tn_gpu = (float)(tn_gpu[0])
                                tn_worker = (float)(tn_worker)
                                tbatch_size = (float)(tbatch_size)
                                tspeed = []
                                tspeed.append((float)(tline[1][1:-2]))
                                #print(n_ps, n_gpu, n_worker, batch_size, speed)
                               # print(tn_ps, tn_gpu, tn_worker, tbatch_size, tspeed)
                                accuracy = sess.run([acc_sum], feed_dict={input_:[[tn_ps, tn_worker, tbatch_size, tn_gpu]], output_:tspeed})
                               # print("ACCURACY : %.3f" %accuracy[0])
                               # print("predict value : %.3f, real value : %.3f" %(tspeed + accuracy[0], tspeed[0]))
                                if abs(accuracy[0] / tspeed) < 0.1:
                                    difference += 1.0
                            print("[Test] accuracy : %.3f percent" % (difference / num_test_data * 100))
                    index += 1
        save_path = saver.save(sess, "/home/jwl1993/Dropbox/term_project_HPC/model.ckpt")



