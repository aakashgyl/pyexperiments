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
    list1.printLLIter()


list1 = None

if __name__ == '__main__':
    initializeLL()