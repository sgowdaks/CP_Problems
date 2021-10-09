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
            
    def reverse(self):
        prev = None
        current = self.root
        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.root = prev
        
        
    def reverselist(self,head):
        
        if head is None or head.next is None:
            return head
            
        rest = self.reverselist(head.next)
        head.next.next = head
        #print(head.data)
        head.next = None
        
        return rest
        
    def addOne(self):
        #Returns new head of linked List.
        self.root = self.reverselist(self.root)
        curr = self.root
        curr.data = curr.data + 1
        carry = 0
        while(curr.next != None and (curr.data > 9 or carry >0)):
            k = (curr.data%10)
            carry = int(curr.data/10)
            curr.data = k
            curr = curr.next
            curr.data = curr.data + carry
            
        if(curr.data > 9):
            k = (curr.data%10)
            carry = int(curr.data/10)
            curr.data = k
            curr.next = node(carry)
            
            
        
        
            
    
        
            
           
linked1 = linkedlist()
linked1.append(9)
linked1.append(9)
linked1.append(9)
# linked1.append("thur")
# linked1.append("friy")
# linked1.append("sun")
#linked1.showtheElem()
#linked1.showtheElem()
linked1.addOne()
#linked1.showtheElem()
#print(linked1.getsize())
#linked1.reverse()
# linked1.showtheElem()
# print("#")
linked1.root = linked1.reverselist(linked1.root)
linked1.showtheElem()

























