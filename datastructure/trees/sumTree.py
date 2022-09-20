class Solution:
    def isSumTree(self,root):
        # Code here
        self.bool = True
        
        def getSum(root):
            if root == None:
                return 0
                
            if root.left == None and root.right == None:
                return root.data
            
            s = getSum(root.left) + getSum(root.right)
            if root.data == s:
                return root.data + s
            else:
                self.bool = False
                return root.data + s
                
                
            
        if root == None:
            return 1
        
        if root.left == None and root.right == None:
            return 1
        
        right = getSum(root.right)
        left = getSum(root.left)
        
        if root.data == (right + left):
            if self.bool:
                return 1
            else:
                return 0
        else:
            return 0
