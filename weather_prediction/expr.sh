#!/bin/bash
# Experiment
for i in 1980 1990 2000 2010; do
	python3 rnn.py  train_data/train_data_${i}-201403 test_data/test_data &> ${i}
	mv rnn.h5 rnn_${i}-201403.h5
done
grep Average *0 >> expr_log

