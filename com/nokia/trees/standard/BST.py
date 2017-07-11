'''
Created on 26-May-2017

@author: aagoyal
'''
from __future__ import print_function
from Node import Node

class BST:
    def __init__(self):
        self.root = None
        self.nodeCount = 0
    
    def addNode(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.searchAndAdd(data, self.root)
        self.nodeCount += 1
        
    def searchAndAdd(self, data, node):        
        if data < node.getValue(): #move to left side
            if node.hasLeft():
                self.searchAndAdd(data, node.getleftAdd())
            else:
                self.addAt(node, "left", data)
        else: #move to right side
            if node.hasRight():
                self.searchAndAdd(data, node.getrightAdd())
            else:
                self.addAt(node, "right", data)

    
    def addAt(self, parent, side, data):
        new_node = Node(data)
        if side == "left":
            parent.setleftAdd(new_node)
        elif side == "right":
            parent.setrightAdd(new_node)
            
    
    def printBST(self, node):
        if node == None:
            return None
        
        data = {"value": node.getValue(),
                "left": self.printBST(node.getleftAdd()),
                "right": self.printBST(node.getrightAdd())
                }
        
        return data
    
    def inorder(self, node):
        if node == None:
            return None
        else:
            self.inorder(node.getleftAdd())
            print(node.getValue(), " -> ", end="")
            self.inorder(node.getrightAdd())
            
    def preorder(self, node):
        if node == None:
            return None
        else:
            print(node.getValue(), " -> ", end="")
            self.preorder(node.getleftAdd())
            self.preorder(node.getrightAdd())
            
    def postorder(self, node):
        if node == None:
            return None
        else:
            self.postorder(node.getleftAdd())
            self.postorder(node.getrightAdd())
            print(node.getValue(), " -> ", end="")
            
    def levelOrderTraversal(self):
        store_level_add = []
        store_level_add_next = []
        store_level_add.append(self.root)
        
        while(store_level_add != []):
            for address in store_level_add:
                print(address.getValue(), " -> ", end = "")
                if address.hasLeft():
                    store_level_add_next.append(address.getleftAdd())
                if address.hasRight():
                    store_level_add_next.append(address.getrightAdd())
                    
            store_level_add = store_level_add_next
            store_level_add_next = []

def prettyprint(datadict):
    print(datadict)


if __name__ == '__main__':
    bst =  BST()
    bst.addNode(400)
    bst.addNode(100)
    bst.addNode(50)
    bst.addNode(200)
    bst.addNode(200)
    bst.addNode(10)
    bst.addNode(20)
    bst.addNode(300)
    bst.addNode(400)
    #bst.addAt(bst.root.getrightAdd(), "right", 3)
    #bst.addAt(bst.root.getrightAdd().getrightAdd(), "right", 4)
    #bst.addAt(bst.root, "left", 0)
    #bst.addNode(4)
    prettyprint(bst.printBST(bst.root))
    print("Inorder: ")
    bst.inorder(bst.root)
    print()
    print("Preorder: ")
    bst.preorder(bst.root)
    print()
    print("Postorder: ")
    bst.postorder(bst.root)
    print()
    print("LevelOrder: ")
    bst.levelOrderTraversal()