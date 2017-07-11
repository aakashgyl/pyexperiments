'''
Created on 23-Jun-2017

@author: aagoyal
'''

def BinarySearch(start, end, arr, sear):
    print start, end
    if(start <= end):
        mid = (start + end)/2
        if arr[mid] == sear:
            print "Found it ", mid
            return mid
        elif arr[mid] < sear:
            start = mid + 1
        else:
            end = mid - 1
        return BinarySearch(start, end, arr, sear)
    else:
        return -1

if __name__ == '__main__':
    arr = [2,4,6,8,10, 12]
    val =  BinarySearch(0, len(arr) - 1, arr, 10)
    print val