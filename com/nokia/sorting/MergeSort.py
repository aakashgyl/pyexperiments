'''
Created on 27-Jun-2017

@author: aagoyal
'''

def MergeSort(arr, start, end):
    if(start < end):
        mid = (start + end)/2
        MergeSort(arr, start, mid)
        MergeSort(arr, mid + 1, end)
        merge(arr, start, mid, end)
        
def merge(arr, start, mid, end):
    

if __name__ == '__main__':
    arr = [64, 25, 13, 12]
    MergeSort(arr, 0 , len(arr)-1)
    print arr