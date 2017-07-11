'''
Created on 26-Jun-2017

@author: aagoyal
'''

#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
def InsertionSort(arr):
    for i in xrange(1, len(arr)):
        j = i - 1
        key = arr[i]
        while(j >= 0 and key < arr[j]):
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
                    
if __name__ == '__main__':
    arr = [64, 25, 22, 11, 9, 8]
    InsertionSort(arr)
    
# Time Complexity: O(n*n)
# 
# Auxiliary Space: O(1)
# 
# Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. 
# And it takes minimum time (Order of n) when elements are already sorted.
# 
# Algorithmic Paradigm: Incremental Approach
# 
# Sorting In Place: Yes
# 
# Stable: Yes
# 
# Online: Yes
# 
# Uses: Insertion sort is used when number of elements is small. 
# It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
# 
# What is Binary Insertion Sort?
# We can use binary search to reduce the number of comparisons in normal insertion sort. 
# Binary Insertion Sort find use binary search to find the proper location to insert the selected item 
# at each iteration. In normal insertion, sort it takes O(i) (at ith iteration) in worst case. 
# We can reduce it to O(logi) by using binary search. 
# The algorithm as a whole still has a running worst case running time of O(n2) because of the series of swaps 
# required for each insertion. Refer this for implementation.