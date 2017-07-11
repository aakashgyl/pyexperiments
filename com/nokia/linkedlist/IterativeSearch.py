'''
Created on 23-May-2017

@author: aagoyal
'''

from com.nokia.linkedlist.standard.LinkedList import LinkedList

def initializeLL():
    global list1
    list1 = LinkedList()
    for i in range(20):
        list1.addNodeAtHead(i)
        
    list1.printLL()

def searchIterLL(curr_Add, elem_value):
    while(curr_Add != None):
        if curr_Add.getValue() == elem_value:
            return True
        else:
            curr_Add = curr_Add.getNextAdd()
    return False
    
list1 = None

if __name__ == '__main__':
    initializeLL()
    print searchIterLL(list1.getHead(), 112)