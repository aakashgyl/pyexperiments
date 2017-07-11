'''
Created on 17-May-2017

@author: aagoyal
'''

class Node():
    def __init__(self):
        self.__value = None
        self.__nextAdd = None
        self.__prevAdd = None
        
    def setValue(self, value):
        self.__value = value
        
    def getValue(self):
        return self.__value
        
    def setPrevAdd(self, prevAdd):
        self.__prevAdd = prevAdd
        
    def getPrevAdd(self):
        return self.__prevAdd
        
    def setNextAdd(self, nextAdd):
        self.__nextAdd = nextAdd
        
    def getNextAdd(self):
        return self.__nextAdd
        
    def hasNext(self):
        return self.__nextAdd != None
    
    def hasPrev(self):
        return self.__prevAdd != None