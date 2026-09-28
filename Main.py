class Iostring:
    def __init__(self):
        self.str=""

    def getstring(self):
        self.str=(input("Enter a string:"))
    
    def printstring(self):
        print("Result is :",self.str.upper())
obj=Iostring()
obj.getstring()
obj.printstring()