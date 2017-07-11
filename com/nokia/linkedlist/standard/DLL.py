'''
Created on 18-May-2017

@author: aagoyal
'''
from __future__ import print_function

from Node import Node

class DLL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def addNode(self, value):
        node = Node()
        node.setValue(value)
        node.setNextAdd(self.head)
        
        if self.head == None:
            self.tail = node
            
        self.head = node
        
        if node.getNextAdd() != None:
            node.getNextAdd().setPrevAdd(node)
            
        self.length += 1
            
    def printDLLHead(self):
        curr_add = self.head
        
        while(curr_add!= None):
            print(curr_add.getValue(), " -> ", end='')
            curr_add = curr_add.getNextAdd()
            
        print()
        
    def printDLLTail(self):
        curr_add = self.tail
        
        while(curr_add != None):
            print(curr_add.getValue(), " -> ", end='')
            curr_add = curr_add.getPrevAdd()
            
        print ()
        
    def deleteAtHead(self):
        self.head = self.head.getNextAdd()
        self.head.setPrevAdd(None)
        
    def deleteAtEnd(self):
        self.tail = self.tail.getPrevAdd()
        self.tail.setNextAdd(None)
    
    def deleteAtPos(self, pos):
        curr_add = self.head
        curr_pos = 0
        
        if(self.length < pos):
            print("Error: Position expected is greater than the passed position...")
            print("Current length of LL -> ", self.length, " and position passed -> ", pos)
            return
        
        if(pos == 0):
            self.deleteAtHead()
            
        elif(pos == self.length):
            self.deleteAtEnd()
            
        else:            
            while(curr_pos != pos): #when this will terminate, we will be on the node that needs to be deleted
                curr_add = curr_add.getNextAdd()
                curr_pos += 1
            curr_add.getPrevAdd().setNextAdd(curr_add.getNextAdd())
            
        self.length -= 1

if __name__ == '__main__':
    list1 = DLL()
    for i in range(20):
        list1.addNode(i)
        #list1.printDLLHead()
        #list1.printDLLTail()
    
    user_input = raw_input("Options: 1. Add node \n2. Delete node  \n3. Exit \nYour choice -> ")
    
    while(user_input != '3'):
        if user_input == '1':
            addAtPos = raw_input("Will add... What position?")
            
        elif user_input == '2':
            delAtPos = raw_input("Will delete... What position?")
            list1.deleteAtPos(int(delAtPos))
            list1.printDLLHead()
            
        user_input = raw_input("Whats next???  ")
    
    print("Exiting.....")