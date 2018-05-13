
import sys
import os

def isIt(line):
    regexes=["0000","0600","1200","1800"]
    for regex in regexes:
        if regex in line[8:12]: 
            return True
    return False 

def readFile(inFile,outFile):

    while True:
        line = inFile.readline().strip()
        if not line:
            break

        if isIt(line):
            print(line, file=outFile)
        else:
            continue


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

    readFile(inFile, outFile)

    inFile.close()
    outFile.close()
