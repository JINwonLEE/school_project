
import sys
import os
import math


def func(x):
    if len(x) >= 10:
        return x
    if x == '':
        return 0
    else:
        return float(x)

def readFile(inFile,outFile):
    data = []
    while True:
        line = inFile.readline().strip()
        if not line:
            break
        line = line.split(',')
        line = list(map(func, line))
        
        data.append(line)
    
    return data

def avg(D, index):
    SUM=0
    N=0
    for i in D:
        SUM += i[index]
        N+=1
    return float(SUM)/float(N)

def std(D, avg, index):
    SUM=0
    N=0
    for i in D:
        SUM += abs(i[index]-avg)*abs(i[index]-avg)
        N+=1
    return math.sqrt(float(SUM)/float(N))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        inFile = open(sys.argv[1], 'r')
        outFile = open(sys.argv[2], 'w')
    elif len(sys.argv) > 1:
        inFile = open(sys.argv[1], 'r')
        outFile = sys.stdout
    else:
        print("Argument Error.")
        exit(0)

    D = readFile(inFile, outFile)
    

    # average 
    avg_list = [0]
    for i in range(1,7):
        average = avg(D,i)
        avg_list.append(average)


    # std
    std_list = [0]
    for i in range(1,7):
        standard = std(D, avg_list[i], i)
        std_list.append(standard)

    # normalize
    for index in range(1,7):
        for row in D:
            row[index] = (row[index]-avg_list[index])/std_list[index]
    
    print(avg_list)    
    print(std_list)
    for line in D:
        print("%s,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" %(line[0], line[1], line[2], line[3], line[4],
            line[5], line[6]))

    inFile.close()
    outFile.close()
