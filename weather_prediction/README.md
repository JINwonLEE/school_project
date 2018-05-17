2018-Spring-Special Topic project.
==================================

Goal
----------
Predicting Future Temperature of Ulsan city 

Features to train
-----------------
Temperature, Precipitation(6hr), wind_speed, wind_direction, humidity, sea level pressure


train_data dir 

	The data in this dir is the ASOS 6-hour data of Ulsan from 1980 to 2017.

	It's provided.

test_data dir

	test_data is 2014~2017 Ulsan City ASOS data. 

	We did take about 5000 data from train data. 


nn.py

	This is a simple neural network with three hidden layers and it exploits all features to predict the regional temperature.

	Each hidden layer consists of 30 nodes and all layers are fully connected.

	So the computation and its output should be very obvious.

	The prediction 

rnn.py

	Data insight : Time series and low correlation between temperature and all other features.

	So, interestingly we here only applied a temperature feature into our RNN model.

	We make a series of sequences from temperature data along with time.




Result
------

	We defined accuracy newly for this work.
	Average Temperature Difference(ATD) = Reduce_mean(absolute value of difference between predicted value and real value)

	Linear Regression
	Average Temperature Difference : 9.18 C degree

	Simple neural network
	Average Temperature Difference : 5.96 C degree

	Simple RNN 
	Average Temperature Difference : 1.49 C degree



Discussion
----------
	Simple RNN models predicted future temperautre very well. 
	We evaluated our RNN using real data. The result is included in our ppt slide. 
	Our prediction matches the range of temperature in reality.






	


