'''
Created on 19-May-2017

@author: aagoyal
'''
from com.nokia.linkedlist.standard.LinkedList import LinkedList

def initializeLL():
    global list1
    list1 = LinkedList()
    for i in range(20):
        list1.addNodeAtHead(i)
        
    list1.printLL()

def searchRecLL(curr_Add, elem_value):
    if curr_Add == None:
        return False
    
    if curr_Add.getValue() == elem_value:
        return True
    
    return searchRecLL(curr_Add.getNextAdd(), elem_value)
    
list1 = None

if __name__ == '__main__':
    initializeLL()
    print searchRecLL(list1.getHead(), 12)