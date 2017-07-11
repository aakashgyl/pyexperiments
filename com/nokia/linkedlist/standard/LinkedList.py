'''
Created on 17-May-2017

@author: aagoyal
'''
from __future__ import print_function
import time
start_time = time.time()

from Node import Node

class LinkedList():
    def __init__(self):
        self.__head = None
        self.__length = 0
        
    def getHead(self):
        return self.__head
    
    def setHead(self, node):
        self.__head = node
        
    def addNodeAtHead(self, value):
        node = Node()
        node.setValue(value)
        node.setNextAdd(self.__head)
        
        self.__head = node
        self.__length += 1
        
    def printLLIter(self):
        curr_add = self.__head
        while(curr_add != None):
            print(curr_add.getValue(), "->", end='')
            curr_add = curr_add.getNextAdd()
        print()
        print("Iterative length now is ", self.getCountIter())
        
    def getCountIter(self):
        curr_add = self.__head
        count = 0
        while(curr_add != None):
            count += 1
            curr_add = curr_add.getNextAdd()
        return count
        
    def printLLRec(self):
        pass
        
        #print("Recursive length now is ", self.getCountRec(self.__head))
        
    def getCountRec(self, curr_add):
        if curr_add == None:
            return 0
        else:
            return 1 + self.getCountRec(curr_add.getNextAdd())
        
    def insertAtPosition(self, pos, value):
        if(pos > self.__length+1):
            print("Position is more than expected... Can't add even at end")
            return
            
        if(pos == 0):
            self.addNodeAtHead(value)
        else:
            curr_add = self.__head
            curr_pos = 0
            while(curr_pos != pos - 1): #at end, will be at node where new one to be inserted at next place
                curr_add = curr_add.getNextAdd()
                curr_pos += 1
            
            node = Node()
            node.setValue(value)
            
            node.setNextAdd(curr_add.getNextAdd())
            curr_add.setNextAdd(node)    
            
        self.__length += 1
            
            
    def deleteAtPosition(self, pos):
        if(pos > self.__length - 1):
            print("Position is more than expected... Can't delete even at end")
            return
        
        if(pos == 0):
            self.__head = self.__head.getNextAdd()
        else:
            curr_add = self.__head
            curr_pos = 0
            while(curr_pos != pos - 1): #at end, will be at node where node to be deleted is at next place
                curr_add = curr_add.getNextAdd()
                curr_pos += 1
                
            if(pos == self.__length):
                curr_add.setNextAdd(None)
            else:
                curr_add.setNextAdd(curr_add.getNextAdd().getNextAdd())
        
            
if __name__ == "__main__":
    list1 = LinkedList()
    for i in range(20):
        list1.addNodeAtHead(i)
        
    list1.printLLIter()
    list1.printLLRec()
     
    user_input = raw_input("Options: 1. Add node \n2. Delete node  \n3. Exit \nYour choice -> ")
     
    while(user_input != '3'):
        if user_input == '1':
            list1.insertAtPosition(input("Will add... What position?"), raw_input("What is the value? "))
            list1.printLLIter()
            list1.printLLRec()
             
        elif user_input == '2':
            list1.deleteAtPosition(input("Will delete... What position?"))
            list1.printLLIter()
            list1.printLLRec()
            
        user_input = raw_input("Whats next???  ")
     
    print("Exiting.....")
    
    #print("--- %s seconds ---" % (time.time() - start_time))