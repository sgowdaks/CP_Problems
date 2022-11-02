#***optimized solution**
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def find(root, x, y, height, parent, dicti):
            if root == None:
                return 0, parent
            if root.val == x:
                dicti[x] = (parent, height)
                return 
            elif root.val == y:
                dicti[y] = (parent, height)
                return 
                
            
            parent = root
            height += 1
            find(root.left,x, y, height, parent, dicti)
            find(root.right, x, y, height, parent, dicti)
        
        height = 0
        parent = root
        dicti = {}
        find(root, x, y, height, parent, dicti)
        if len(dicti) == 1:
            return False
        else:
            root1, height1 = dicti[x]
            root2, height2 = dicti[y]
            if height1 == height2:
                if root1 == root2:
                    return False
                return True
            return False
        
        
#*****************************--------------------****************************

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def find(root, cousin, height, parent):
            if root == None:
                return 0, parent
            if root.val == cousin:
                return height, parent
            
            parent = root
            height += 1
            height1, parent1 = find(root.left, cousin, height, parent)
            height2, parent2 = find(root.right, cousin, height, parent)
            if height1 == 0 and height2 == 0:
                return 0, parent2
            elif height1 != 0:
                return height1, parent1
            elif height2 != 0:
                return height2, parent2
        
        height = 0
        parent = root
        x1, parent1 = find(root, x, height, parent)
        x2, parent2 = find(root, y, height, parent)
                
        if x1 == x2:
            if parent1 == parent2:
                return False
            return True
        else:
            return False
            
            
        
