'''
Created on 17-May-2017

@author: aagoyal
'''

class Node():
    indent = ""
    def __init__(self, value, leftAdd = None, rightAdd = None):
        self.__value = value
        self.__leftAdd = leftAdd
        self.__rightAdd = rightAdd
        
    def __str__(self):
        Node.indent = Node.indent + "    "
        print Node.indent, "Value -> ", self.getValue()
        print Node.indent, "Left  -> ", self.getleftAdd()
        print Node.indent, "Right -> ", self.getrightAdd()
        return ""
        
    def setValue(self, value):
        self.__value = value
        
    def getValue(self):
        return self.__value
        
    def setrightAdd(self, rightAdd):
        self.__rightAdd = rightAdd
        
    def getrightAdd(self):
        return self.__rightAdd
        
    def setleftAdd(self, leftAdd):
        self.__leftAdd = leftAdd
        
    def getleftAdd(self):
        return self.__leftAdd
        
    def hasLeft(self):
        return self.__leftAdd != None
    
    def hasRight(self):
        return self.__rightAdd != None