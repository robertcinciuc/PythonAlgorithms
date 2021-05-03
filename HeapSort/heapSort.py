import math
import os

def heapify( arr ):
    return 0


def heapInsert( arr ):

    myHeap = [None]*len(arr)
    for i, elem in enumerate(arr):
        
        myHeap[i] = elem
        found = False
        dadPos = int((i - (2-i%2))/2)
        pos = i
        
        # Bottom-up search until the correct place found
        while( not found ):
            if( pos == 0 ):
                found = True

            elif( myHeap[dadPos] < elem ):
                myHeap[pos] = myHeap[dadPos]
                myHeap[dadPos] = elem
                pos = dadPos
                dadPos = int((pos - (2-pos%2))/2)
                
            elif( myHeap[dadPos] >= elem ):
                found = True

    return myHeap


def heapDelete( myHeap ):

    i = 0
    while(i < len(myHeap)):

        maxi = myHeap[0]
        myHeap[0] = myHeap[len(myHeap)-i-1]
        found = False
        pos = 0

        # Top-down search untill correct place found
        while( not found ):
            if( pos*2 >= len(myHeap)-i-1):
                found = True

            else:
                maxChild = myHeap[ pos*2 + 1 ]
                maxChildPos = pos*2 + 1
                if( myHeap[pos*2 + 2] > maxChild and pos*2 + 2 < len(myHeap)-i):
                    maxChild = myHeap[pos*2 + 2]
                    maxChildPos = pos*2 + 2
                
                if(maxChild > myHeap[pos]):
                    tmp = myHeap[pos]
                    myHeap[pos] = myHeap[maxChildPos]
                    myHeap[maxChildPos] = tmp

                    pos = maxChildPos
            
                else:
                    found = True

        myHeap[len(myHeap)-i-1] = maxi
        i += 1

    return myHeap

if __name__ == '__main__':

    myList = list( map(int, input().rstrip().split() ))

    myHeap = heapInsert( myList )
    sortedList = heapDelete( myHeap )

    print(sortedList)