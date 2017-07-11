'''
Created on 25-May-2017

@author: aagoyal
'''
from com.nokia.trees.standard.Node import Node

class BinaryTree:
    def __init__(self, data):
        self.root =  Node(data)
        
    def printBT(self):
        print self.root
        
    def addNode(self, data):
        self.search(self.root)
        
    def search(self, node):
        if(not node.hasLeft()):
            return node, "left"
        elif(not node.hasRight()):
            return node, "right"
        else:
            self.search(node.getleftAdd())
            self.search(node.getrightAdd())        
    

if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.root.setleftAdd(Node(2))
    tree.root.setrightAdd(Node(3))
    tree.root.getleftAdd().setleftAdd(Node(4))
    
    tree.printBT()