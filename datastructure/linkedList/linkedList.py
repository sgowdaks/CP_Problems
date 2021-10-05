class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.root = None
        self.present = None
        
    def append(self,val):
        if self.root == None:
            self.root = node(val)
            self.present = self.root
        else:
            
            self.present.next = node(val)
            self.present = self.present.next
            
            
            
        
        
    def showtheElem(self):
        printval = self.root
        while(printval != None):
            print(printval.data)
            printval = printval.next
            
    def getsize(self):
        printval = self.root
        size = 0
        while(printval != None):
            #print(printval.data)
            printval = printval.next
            size = size + 1
            
        return size
            
    def inserting(self,val,i):
        printval = self.root
        k = self.getsize()
        size = 0
        if(i == 0):
            val.next = printval
            self.root = val
        else:
            while(size < i-1):
                printval = printval.next
                #print(printval.data)
                size = size+1
            e = val
            k = printval.next
            printval.next = val
            if(k != None):
                printval.next.next = k
                
    def deleting(self,i):
        printval = self.root
        size = 0
        if(i == 0):
            self.root = printval.next
            printval.next = None
        else:
            while(size < i-1):
                printval = printval.next
                size = size+1
            #print(printval.data)
            k = printval.next.next
            printval.next = k
            
            
            
        
        
        
        
linked1 = linkedlist()
#linked1.create()
linked1.append("mon")
linked1.append("tue")
linked1.append("wed")
linked1.append("thur")
linked1.append("friy")
linked1.append("sun")
# linked1.root = node("mon")
# e2 = node("tue")
# e3 = node("wed")
# e4 = node("fri")
# linked1.root.next = e2
# e2.next = e3
# e3.next = e4
linked1.showtheElem()
print(linked1.getsize())
linked1.inserting(node("thur"),0)
linked1.inserting(node("sun"),1)
linked1.inserting(node("sat"),6)
#linked1.showtheElem()
linked1.deleting(2)
linked1.showtheElem()






    
