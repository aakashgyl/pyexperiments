'''
Created on 23-May-2017

@author: aagoyal
'''
#http://www.geeksforgeeks.org/swap-nodes-in-a-linked-list-without-swapping-data/

from com.nokia.linkedlist.standard.LinkedList import LinkedList

def initializeLL():
    global list1
    list1 = LinkedList()
    for i in range(20):
        list1.addNodeAtHead(i)
    list1.printLLIter()

def swap(data1, data2):
    if list1.getCountIter() < 2:
        raise ValueError('Linked List size is much less')
    else:
        prev_firstdata, prev_seconddata = getPrevNodeData()
        swapTheNodes(prev_firstdata,prev_seconddata)
        list1.printLLIter()

def getPrevNodeData():
    curr_add = list1.getHead()
    prev_firstdata = None
    prev_seconddata = None
    
    #handle case if either is head
    if(curr_add.getValue() == data1):
        prev_firstdata = 0
    if(curr_add.getValue() == data2):
        prev_seconddata = 0
    
    while(curr_add.getNextAdd() != None):
        next_val = curr_add.getNextAdd().getValue()
        if(prev_firstdata == None and next_val == data1):
            prev_firstdata = curr_add 
        elif (prev_seconddata == None and next_val == data2):
            prev_seconddata = curr_add
        curr_add = curr_add.getNextAdd()
    
    if (prev_firstdata == None or prev_seconddata == None):
        raise ValueError('Either or both are not present in the linked list')
    
    #print prev_firstdata.getNextAdd().getValue(), prev_seconddata.getNextAdd().getValue()
    
    return prev_firstdata, prev_seconddata

def swapTheNodes(prev_firstdata,prev_seconddata):
    if (prev_seconddata == 0):
        first_add = list1.getHead()
        nextOfFirst = list1.getHead().getNextAdd()
    else:
        first_add = prev_seconddata.getNextAdd()
        nextOfFirst = prev_seconddata.getNextAdd().getNextAdd()
        
    second_add = prev_firstdata.getNextAdd()    
    nextOfSecond = prev_firstdata.getNextAdd().getNextAdd()
    
    if (prev_seconddata == 0):
        list1.getHead().setNextAdd(nextOfSecond)
        list1.setHead(second_add)
    else:
        prev_seconddata.getNextAdd().setNextAdd(nextOfSecond)
        prev_seconddata.setNextAdd(second_add)
        
    prev_firstdata.getNextAdd().setNextAdd(nextOfFirst)
    prev_firstdata.setNextAdd(first_add)
    

list1 = None

if __name__ == '__main__':
    initializeLL()
    data1 = 0
    data2 = 19
    try:
        swap(data1, data2)
    except ValueError as error:
        print error.args
        #raise