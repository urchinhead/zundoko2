#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import sys
import time
import random
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, FileTransferSpeed, FormatLabel, Percentage, ProgressBar, ReverseBar, RotatingMarker, SimpleProgress, Timer, AdaptiveETA, AbsoluteETA, AdaptiveTransferSpeed

maxtest = 1000000
scale = 1000
pattern = [1,0,0,0,0]
words=["ズン","ドコ"]

class myq:

    def __init__(self):                  # コンストラクタ
        self.Q = ['','','','',''] 

    def setQ(self,item):
        self.Q[4]=self.Q[3]
        self.Q[3]=self.Q[2]
        self.Q[2]=self.Q[1]
        self.Q[1]=self.Q[0]
        self.Q[0]=item
        return True

    def checkQ(self):
        if (self.Q[0] == pattern[0]) and \
           (self.Q[1] == pattern[1]) and \
           (self.Q[2] == pattern[2]) and \
           (self.Q[3] == pattern[3]) and \
           (self.Q[4] == pattern[4]):
            
            #print("ヒ・ロ・シ!") 
            return True 

def findmax(testresult):
    maxcount = 0
    for i in testresult:
        if i > maxcount:
            maxcount = i
    return maxcount

       
def calcount(testresult):
    calresult = []
    maxcount = findmax(testresult)

    for i in range(maxcount):
        calresult.append(0)


    for item in testresult:
        calresult[item-1] += 1

    return calresult

if __name__ == "__main__":

    testresult = []

    pbar = ProgressBar(widgets=[Percentage(), Bar()], max_value=maxtest).start()

    for test in range(maxtest):
        q = myq()
        count = 0
        while 1:
            item = random.randint(0,1)
            
            if q.setQ(item):
                #print(words[item])
                count += 1 
            if q.checkQ():
                break
        testresult.append(count)

        pbar.update(test+1) 

    pbar.finish()

    #print(testresult)

    calresult = calcount(testresult)
    
    j = 0 
    for item in calresult:
        j += 1
        print("{0:5d}:{1:6d}[{2:2.2f}%] ".format(j,item,100*item/maxtest),end='')
        for k in range(int(item/scale)):
                print("*", end='')

        print("")


