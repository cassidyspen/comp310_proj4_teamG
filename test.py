import LCG_TeamG
#import pandas as pd # let's us work with data structures
#import numpy as np # let's us do complex things with numbers
#import matplotlib as plt #let's us plot stuff
#from matplotlib import pyplot

import datetime

today = datetime.datetime.now()
now = today.second

def mean(numList):
    y = 0
    for x in numList:
        y = x + y
    return y/280

def numAmt(numList):
    numNums = []
    x = 0
    for x in range(28):
        numNums.append(numList.count(x))
        x+=1
    return numNums


"""def hist():
    plt.pyplot.hist(df["deaths"])
    # set x/y labels and plot title what are they?
    plt.pyplot.xlabel("number of deaths")
    plt.pyplot.ylabel("count")
    plt.pyplot.title("Death bins")"""

if __name__ == "__main__":
    numList = []
    for i in range(1000000):
        now = LCG_TeamG.LCG_TeamG(now)
        numList.append(now%28)
    #print (numList)
    print(numAmt(numList))
