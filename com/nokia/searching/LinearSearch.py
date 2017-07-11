'''
Created on 23-Jun-2017

@author: aagoyal
'''

def LinearSearch(sear, arr):
    count = 0
    for val in arr:
        if sear ==  val:
            return count
        count = count +1 

if __name__ == '__main__':
    array1 = [1,4,7,2,5,4]
    print LinearSearch(5, array1)