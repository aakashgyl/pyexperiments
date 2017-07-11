'''
Created on 23-May-2017

@author: aagoyal
'''
#http://www.geeksforgeeks.org/write-a-function-to-reverse-the-nodes-of-a-linked-list/

from com.nokia.linkedlist.standard.LinkedList import LinkedList

def initializeLL():
    global list1
    list1 = LinkedList()
    for i in range(20):
        list1.addNodeAtHead(i)
    list1.printLLIter()

def reverse():
    old_prev = None
    curr_add = list1.getHead()
    old_next = None
    
    while(curr_add != None):
        old_next = curr_add.getNextAdd()
        curr_add.setNextAdd(old_prev)
        old_prev = curr_add
        curr_add = old_next
        
    list1.setHead(old_prev)

list1 = None

if __name__ == '__main__':
    initializeLL()
    reverse()
    list1.printLLIter()