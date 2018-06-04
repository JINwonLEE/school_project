import pandas as pd
import tensorflow as tf

data = pd.read_csv("data_list.csv")
test = pd.read_csv("test_list.csv")

len_output_class = len(data.groupby('Cancer_Type').groups.keys())
r = data.iterrows()
test_r = test.iterrows()

batch_num = 128
columns = 5
hidden = 128
hidden2 = 64
hidden3 = 32
hidden4 = 16
num_epoch = 10

out_columns = len_output_class

#make Output Column
#Return is_data_finish, batch_input
def get_next_batch(batch, it, d):
    index = 0
    input_ = []
    output_ = []
    for _, row in it:
        index += 1
        row['Chromosome'] = (float)(row['Chromosome'])

        input_.append([float(row['Gene_Name']),row['Chromosome'],float(row['Start_Position']), -float(row['Start_Position']) + float(row['End_Position']), float(row['Variant_Type'])])
        hot_v = []
        for i in range(len_output_class):
            if i == row['Cancer_Type'] :
                hot_v.append(1.0)
            else :
                hot_v.append(0.0)
        output_.append(hot_v)

        if index == batch:
            return False, input_, output_
    return True, input_, output_


x = tf.placeholder(tf.float32, [None, columns])
y = tf.placeholder(tf.float32, [None, out_columns])

global_step = tf.Variable(0, dtype=tf.int64, name='global_step', trainable=False)

W_fc = tf.Variable(tf.truncated_normal([columns, hidden], stddev=0.1))
b_fc = tf.Variable(tf.constant(0.5, shape=[hidden]))

h_fc = tf.nn.relu(tf.matmul(x, W_fc) + b_fc)

W_fc1 = tf.Variable(tf.truncated_normal([hidden, hidden2], stddev=0.1))
b_fc1 = tf.Variable(tf.constant(0.1, shape=[hidden2]))

h_fc1 = tf.nn.relu(tf.matmul(h_fc, W_fc1) + b_fc1)

W_fc2 = tf.Variable(tf.truncated_normal([hidden2, hidden3], stddev=0.1))
b_fc2 = tf.Variable(tf.constant(0.1, shape=[hidden3]))

keep = tf.placeholder(tf.float32)
h_fc2 = tf.nn.dropout(tf.matmul(h_fc1, W_fc2) + b_fc2, keep)

W_fc3 = tf.Variable(tf.truncated_normal([hidden3, hidden4], stddev=0.1))
b_fc3 = tf.Variable(tf.constant(0.1, shape=[hidden4]))

h_fc3 = tf.nn.sigmoid(tf.matmul(h_fc2, W_fc3) + b_fc3)

W_fc4 = tf.Variable(tf.truncated_normal([hidden4, out_columns], stddev=0.1))
b_fc4 = tf.Variable(tf.constant(0.1, shape=[out_columns]))

h_fc4 = tf.matmul(h_fc3, W_fc4) + b_fc4





cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=h_fc4)

cross_entropy = tf.reduce_mean(cross_entropy)

train_op = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy, global_step)

correct_prediction = tf.equal(tf.argmax(h_fc3, 1), tf.argmax(y, 1))
correct_prediction = tf.cast(correct_prediction, tf.float32)

accuracy = tf.reduce_mean(correct_prediction)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    epoch_index = 0
    train_step = 0
    while epoch_index != num_epoch:
        epoch_done, batch_in, batch_out = get_next_batch(batch_num, r, data)
        if train_step % 1000 == 0:
            test_ind = 0
            sum = 0.0
            loss_sum = 0.0
            test_done = False
            while test_done != True:
                test_done, test_batch_in, test_batch_out = get_next_batch(batch_num, test_r, test)
                [loss, test_acc] = sess.run([cross_entropy, accuracy], feed_dict={x:test_batch_in, y:test_batch_out, keep:1.0})
                sum += test_acc
                loss_sum += loss
                test_ind += 1
            print("------------------sum : %.4f, test_ind : %d, loss : %.4f" %(sum, test_ind, loss_sum / float(test_ind)))

            if test_done:
                print("------------------------------- Epoch %i, Train Step %i Test Accuracy : %.4f" %(epoch_index, train_step, (float)(sum)/(float)(test_ind)))
                test_r = test.iterrows()

        loss, _,train_acc = sess.run([cross_entropy, train_op, accuracy], feed_dict={x:batch_in, y:batch_out, keep:0.5})
        if train_step % 100 == 0:
            print("Epoch %i, Train Step %i Train loss : %.4f, Train Accuracy : %.4f" %(epoch_index, train_step, loss, train_acc))

        train_step += 1
        if epoch_done:
            epoch_index += 1
            train_step = 0
            r = data.iterrows()








