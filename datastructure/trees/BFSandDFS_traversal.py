class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key
 
    
def PreOrder(m):
    if(m):
        print(m.key)
        PreOrder(m.left)
        PreOrder(m.right)
        
def PostOrder(m):
    if(m):
        PostOrder(m.left)
        PostOrder(m.right)
        print(m.key)
           
def InOrder(m):
    if(m):
        PostOrder(m.left)
        print(m.key)
        PostOrder(m.right)
        
def BFT(k):
    q = []
    tra = []
    if(k == None):
        return 
    q.append(k)
    while(len(q) > 0):
        k = q.pop(0)
        tra.append(k.key)
        if k.left != None:
            q.append(k.left)
        if k.right != None:
            q.append(k.right)
        #print(len(q))
    
    return tra
    
  
k = Node(1)
k.left = Node(2)
k.right = Node(3)
k.left.left = Node(4)
k.left.right = Node(5)
k.right.left = Node(6)
k.right.right = Node(7)
print("PreOrder")
PreOrder(k)
print("PostOrder")
PostOrder(k)
print("InOrder")
InOrder(k)
print("Breadth search tree")
print(BFT(k))
