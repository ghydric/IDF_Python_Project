# This is a class to define the helpObject
# This should allow us to read in data from a text file and objectify it

class HelpObject:
    def __init__(self, desc, ex1, ex2):
        self.__desc = desc
        self.__ex1 = ex1
        self.__ex2 = ex2

# Class settors
    def setDesc(self, desc):
        self.__desc = desc

    def setEx1(self, ex1):
        self.__ex1 = ex1
    
    def setEx2(self, ex2):
        self.__ex2 = ex2

# Class Gettors
    def getDesc(self):
        return self.__desc
    
    def getEx1(self):
        return self.__ex1
    
    def getEx2(self):
        return self.__ex2
        
# This has been tested locally for functionality.
