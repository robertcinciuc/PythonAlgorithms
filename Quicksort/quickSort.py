import math 
import os

def quickSort( arr ):

    if(len(arr) <= 1):
        return arr
    
    elif(len(arr) == 2):
        if(arr[0] > arr[1]):
            tmp = arr[1]
            arr[1] = arr[0]
            arr[0] = tmp

        return arr
    
    else:
        index = 0
        biggerRight = len(arr) - 2
        foundBig = False
        while(index <= biggerRight):
            if(arr[index] >= arr[len(arr) - 1]):
                tmp = arr[biggerRight]
                arr[biggerRight] = arr[index]
                arr[index] = tmp
                biggerRight -= 1
                foundBig = True
            else:
                index += 1
        
        if(foundBig):
            tmp = arr[len(arr) - 1]
            arr[len(arr) - 1] = arr[index]
            arr[index] = tmp

            if(index == 0):
                index = 1

            first = quickSort(arr[:index])
            second = quickSort(arr[index:])
            
            tmp = first.copy()
            tmp.extend(second)

            return tmp
        
        else:
            first = quickSort(arr[:len(arr)-1])
            second = quickSort(arr[len(arr)-1:])

            tmp = first.copy()
            tmp.extend(second)

            return tmp

if __name__ == '__main__':

    myList = list(map(int, input().rstrip().split() ))

    sortedList = quickSort(myList)

    print("final list")
    print(sortedList)