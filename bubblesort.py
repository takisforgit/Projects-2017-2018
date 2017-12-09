# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:33:21 2017

@author: takis
"""
import time


def bubbleSort(alist):
    swaps=0
    comparisons=0
    for passnum in range(len(alist)-1,0,-1):
        print("\nPass No.:", len(alist)-passnum,"\n")
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                print("Comparing %3d - %3d"% (alist[i],alist[i+1]), end="")
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                swaps +=1
                comparisons +=1
                print("  --->  Swaped: %3d with %3d"%(temp, alist[i]  ))
                print(alist)
            else:
                print("Comparing %3d - %3d"% (alist[i],alist[i+1]))
                comparisons +=1

            time.sleep(2)
        passnum = passnum-1
    return(swaps, comparisons)


alist=[110,20,40,90,30, 50,70,80,100,60]
myswaps=[]
print("Initial LIST")
print(alist,"\n")
myswaps=bubbleSort(alist)
#print(myswaps)
print("List SORTED !", alist)
print()
print("Swaps: %d , Comparisons: %d"%(myswaps))