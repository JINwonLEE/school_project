import pandas as pd
import tensorflow as tf

data = pd.read_csv("data_list.csv")
test = pd.read_csv("test_list.csv")

r = data.iterrows()

batch = 50
columns = 8
hidden = 10
out_columns = 1

#make Output Column
#Return is_data_finish, batch_input
def get_next_data(batch):
    index = 0
    input_ = []
    for _, row in r:
        index += 1
        if row['Chromosome'] == 'X':
            row['Chromosome'] = -1.0
        else:
            row['Chromosome'] = (float)(row['Chromosome'])

        input_.append([float(row['Cancer_Type']), float(row['Tumor_Sample_ID']), float(row['Gene_Name']), \
                row['Chromosome'], float(row['Start_Position']), float(row['End_Position']), float(row['Variant_Type']), \
                float(row['Reference_Allele']), float(row['Tumor_Allele'])])

        if index == batch:
            return False, input_
    return True, input_


x = tf.placeholder(tf.float32, [None, columns])
y = tf.placeholder(tf.float32, [None, out_columns])

global_step = tf.Variable(0, dtype=tf.int64, name='global_step', trainable=False)

W_fc = tf.Variable(tf.truncated_normal([columns, hidden], stddev=0.1))
b_fc = tf.Variable(tf.constant(0.1, [-1, hidden]))

h_fc = tf.nn.relu(tf.matmul(x, W_fc) + b_fc)

W_fc2 = tf.Variable(tf.truncated_normal([hidden, out_columns], stddev=0.1))
b_fc2 = tf.Variable(tf.constant(0.1, [-1, out_columns]))

h_fc2 = tf.matmul(h_fc, W_fc2) + b_fc2

cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=h_fc2)

cross_entropy = tf.reduce_mean(cross_entropy)

train_op = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy, global_step)

correct_prediction = 



print(get_next_data(3))
print(get_next_data(3))


