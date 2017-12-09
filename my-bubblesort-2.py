# -*- coding: utf-8 -*-
"""
Created on Mon Oct 2 22:33:21 2017
COORECT VERSION FOR Short BUBBLE-SHORT - Fewer Passes (NOT n-1)
@author: takis
"""

import time

def bubbleSort(array) :
    isSorted = False
    temporaryReference = 0
    index=0
    passnum=1
      
    while(not isSorted) :
        
        isSorted = True
        print("\nPass No.:", passnum,"\n")
        ## Iterate until we get to the last element
        ## After each pass we know that the last element is in corect position
        ## So DON'T check it !!!
        
        for index in range(len(array)-passnum) :
            print("Comparing  %d and %d "%(array[index] , array[index+1]))
          
          ## If the element to the left is bigger, then swap the element
          ## that we're currently looking at with its left neighbor.
            if (array[index] > array[index+1] ) :
                isSorted = False
                print("SWAPPING %d and %d  --> " %(array[index] , array[index +1]), end="")
            
            ## Swap elements by creating a temporary reference.
                temp = array[index]
                array[index] = array[index+1]
                array[index+1] = temp
          
                print('array is now ', array)
                printArrayVertHistogram(array)
            time.sleep(2)
        passnum += 1
        print("***is array sorted? ", isSorted)
      
  
def printArrayVertHistogram(array) :
    
    maxim = max(array)
    for cursor in range(maxim) :
      
        for item in array:
            #  maxim - cursor is position count
            if ( maxim - cursor  <= int(item) ):
                print ('|', end="")
            else:
                print(' ', end="")
    ##            print('-', end="")
        print()


    


myArray = [9, 7, 4, 1, 2, 10, 8, 12, 5]
print(myArray)
printArrayVertHistogram(myArray)
bubbleSort(myArray)
