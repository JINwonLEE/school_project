import numpy as np
from math import sin, cos, hypot, atan2, radians
import json

ADO_X = 34.550461
ADO_Y = -117.433907
RPV_X = 33.743462
RPV_Y = -118.404121
RSS_X = 33.97327
RSS_Y = -117.326736
USC_X = 34.019192
USC_Y = -118.286308


data = np.loadtxt("csv_file/NN_test_X.csv", delimiter=",")


output = {}
line_list = []
for idx ,line in enumerate(data):
    tuple = []
    for i in range(10):
        x_, y_ = line[2*i], line[2*i+1]
        arrive_time = line[29 + i]
        
        x_lad = radians(x_)
        y_lad = radians(y_)
        ad_x_lad = radians(ADO_X)
        ad_y_lad = radians(ADO_Y)
        rp_x_lad = radians(RPV_X)
        rp_y_lad = radians(RPV_Y)
        rs_x_lad = radians(RSS_X)
        rs_y_lad = radians(RSS_Y)
        us_x_lad = radians(USC_X)
        us_y_lad = radians(USC_Y)

        Earth_R = 6371.0

        ad_x = ( ad_y_lad - y_lad ) * cos( 0.5 * ( ad_x_lad + x_lad ) )
        ad_y = ad_y_lad - y_lad
        ad_dist = Earth_R * hypot(ad_x, ad_y) #km
        tuple.append(ad_dist)


        rp_x = ( rp_y_lad - y_lad ) * cos( 0.5 * ( rp_x_lad + x_lad ) )
        rp_y = rp_y_lad - y_lad
        rp_dist = Earth_R * hypot(rp_x, rp_y) #km
        tuple.append(rp_dist)


        rs_x = ( rs_y_lad - y_lad ) * cos( 0.5 * ( rs_x_lad + x_lad ) )
        rs_y = rs_y_lad - y_lad
        rs_dist = Earth_R * hypot(rs_x, rs_y) #km
        tuple.append(rs_dist)


        us_x = ( us_y_lad - y_lad ) * cos( 0.5 * ( us_x_lad + x_lad ) )
        us_y = us_y_lad - y_lad
        us_dist = Earth_R * hypot(us_x, us_y) #km
        tuple.append(us_dist)
        tuple.append(arrive_time)

    output[idx] = tuple


out = open("data_set", "w")
json.dump(output, out)

