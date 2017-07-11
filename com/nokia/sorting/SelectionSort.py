'''
Created on 26-Jun-2017

@author: aagoyal
'''
#repeatedly finding the minimum element (considering ascending order) from unsorted part
# and putting it at the beginning.
def SelectionSort(arr):
    for count in xrange(len(arr)):
        mini = count
        for count2 in xrange(len(arr) - count):
            if arr[count2 + count] < arr[mini]:
                mini = count + count2
                
        arr[count], arr[mini] = arr[mini], arr[count]   

if __name__ == '__main__':
    arr = [64, 25, 22, 11, 9, 8]
    print arr
    SelectionSort(arr)
    
# Time Complexity: O(n2) as there are two nested loops. (All cases)

# Auxiliary Space: O(1)
# The good thing about selection sort is it never makes more than O(n) swaps 
# and can be useful when memory write is a costly operation.