##
## Print Vertcal Histogram of number of letters of words in a phrase
##

##phrase = input("Enter a phrase: ")
##words = phrase.split()
##max_length = len(max(words, key=len)) # length of longest word
##for cursor in range(max_length):
##  
##    for word in words:
##        # max_length - cursor is position count
##        if (max_length - cursor) <= len(word):
##            print ('*', end="")
##        else:
##            print('', end="")
####            print('-', end="")
##    print()


array=[ 7, 4, 5, 8, 10]

def printArrayVertHistogram(array) :
    
    maxim = max(array)
    for cursor in range(maxim) :
      
        for item in array:
            #  maxim - cursor is position count
            if ( maxim - cursor  <= int(item) ):
                print ('*', end="")
            else:
                print(' ', end="")
    ##            print('-', end="")
        print()


printArrayVertHistogram(array)
    
