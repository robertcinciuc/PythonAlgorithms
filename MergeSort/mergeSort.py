import math
import os

def merge(left, right):

    i = 0
    j = 0
    res = []
    while( i < len(left) and j < len(right)):
        if( left[i] < right[j] ):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    if(i < len(left) ):
        for ii in range(i, len(left)):
            res.append(left[ii])

    elif( j < len(right) ):
        for jj in range(j, len(right)):
            res.append(right[jj])

    return res

def mergeSort(arr, l, r):

    if( r - l > 1 ):

        m = int((r - l)/2) + l

        left = mergeSort(arr, l, m)
        right = mergeSort(arr, m, r)
        
        res = merge(left, right)
        
        return res
    
    else:
        res = []
        res.append(arr[l])
        return res


if __name__ == '__main__' :

    myList = list( map(int, input().rstrip().split() ) )

    newList = mergeSort(myList, 0, len(myList))

    print(newList)

