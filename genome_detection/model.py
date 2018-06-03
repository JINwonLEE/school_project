import pandas as pd
import tensorflow as tf

data = pd.read_csv("data_list.csv")
test = pd.read_csv("test_list.csv")

len_output_class = len(data.groupby('Cancer_Type').groups.keys())
r = data.iterrows()
test_r = test.iterrows()

batch_num = 500
columns = 8
hidden = 10
num_epoch = 10

out_columns = len_output_class

#make Output Column
#Return is_data_finish, batch_input
def get_next_batch(batch, it):
    index = 0
    input_ = []
    output_ = []
    for _, row in it:
        index += 1
        if row['Chromosome'] == 'X' :
            row['Chromosome'] = -1.0
        elif row['Chromosome'] == 'GL000209.1':
            row['Chromosome'] = -1.5
        elif row['Chromosome'] == 'MT':
            row['Chromosome'] = -2.0
        elif row['Chromosome'] == 'Y':
            row['Chromosome'] = -2.5
        elif row['Chromosome'] == 'GL000213.1':
            row['Chromosome'] = -3.0
        elif row['Chromosome'] == 'GL000192.1':
            row['Chromosome'] = -3.5
        elif row['Chromosome'] == 'GL000212.1':
            row['Chromosome'] = -4.0
        elif row['Chromosome'] == 'GL000218.1':
            row['Chromosome'] = -4.5
        elif row['Chromosome'] == 'GL000205.1':
            row['Chromosome'] = -5.0
        else:
            row['Chromosome'] = (float)(row['Chromosome'])

        input_.append([float(row['Tumor_Sample_ID']), float(row['Gene_Name']), \
                row['Chromosome'], float(row['Start_Position']), float(row['End_Position']), float(row['Variant_Type']), \
                float(row['Reference_Allele']), float(row['Tumor_Allele'])])
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
b_fc = tf.Variable(tf.constant(0.1, shape=[hidden]))

h_fc = tf.nn.tanh(tf.matmul(x, W_fc) + b_fc)

W_fc2 = tf.Variable(tf.truncated_normal([hidden, out_columns], stddev=0.1))
b_fc2 = tf.Variable(tf.constant(0.1, shape=[out_columns]))

h_fc2 = tf.matmul(h_fc, W_fc2) + b_fc2

cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=h_fc2)

cross_entropy = tf.reduce_mean(cross_entropy)

train_op = tf.train.RMSPropOptimizer(1e-4).minimize(cross_entropy, global_step)

correct_prediction = tf.equal(tf.argmax(h_fc2, 1), tf.argmax(y, 1))
correct_prediction = tf.cast(correct_prediction, tf.float32)

accuracy = tf.reduce_mean(correct_prediction)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    epoch_index = 0
    train_step = 0
    while epoch_index != num_epoch:
        epoch_done, batch_in, batch_out = get_next_batch(batch_num, r)
        if train_step % 100 == 0:
            test_done, test_batch_in, test_batch_out = get_next_batch(batch_num, test_r)
            test_acc = accuracy.eval(feed_dict={x:test_batch_in, y:test_batch_out})
            print("Epoch %i, Train Step %i Test Accuracy : %g" %(epoch_index, train_step, test_acc))

        loss, _,train_acc = sess.run([cross_entropy, train_op, accuracy], feed_dict={x:batch_in, y:batch_out})
        if train_step % 50 == 0:
            print("Epoch %i, Train Step %i Train loss : %.4f" %(epoch_index, train_step, loss))
            #print("Epoch %i, Train Step %i Train Accuracy : %g" %(epoch_index, train_step, train_acc))

        train_step += 1
        if epoch_done:
            epoch_index += 1
            train_step = 0
            r = data.iterrows()

        if test_done:
            test_r = test.iterrows()








