# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:33:21 2017
COORECT VERSION FOR Short BUBBLE-SHORT - Fewer Passes (NOT n-1)
@author: takis
"""
import time

def shortBubbleSort(alist):
    exchanges = True
    passnum = 1
    swaps=0
    comparisons=0
    while passnum > 0  and exchanges :

       print("\nPass No.:", passnum,"\n")
       exchanges = False
       for i in range(len(alist)-passnum ):

           if alist[i]>alist[i+1]:
               print("Comparing %3d - %3d"% (alist[i],alist[i+1]), end="")
               exchanges = True
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
       passnum = passnum+1
    return(swaps, comparisons)

alist=[110,20,40,90,30, 50,70,80,100,60]
myswaps=[]
print("Initial LIST")
print(alist,"\n")
myswaps=shortBubbleSort(alist)
#print(myswaps)
print("List SORTED !", alist)
print()
print("Swaps: %d , Comparisons: %d"%(myswaps))
