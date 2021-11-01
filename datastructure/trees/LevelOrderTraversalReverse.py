class Node:
    def __init__(self,root):
        self.data = root
        self.right = None
        self.left = None

# Driver program to test above function 
def printLevelOrder(root):
    h = height(root)
    #print(h)
    k = 0
    for i in range(1,h+1):
        #h = h - k
        #print(h,k)
        #print(i,h)
        traversal(root,i,h)
        #k = k+1
        
def traversal(root,level,height):
    if root == None:
        return 0
    
    if(level == height ):
        print(root.data)
    else:
        traversal(root.left,level+1,height)
        traversal(root.right,level+1,height)
      
    
    
    
def height(root):
    if root == None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
            
    
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
root.right.left = Node(6) 
root.right.right = Node(7) 

print("Level order traversal")
printLevelOrder(root) 
