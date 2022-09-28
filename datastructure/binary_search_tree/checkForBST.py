class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traversal(root, left, right):
            if root == None:
                return True
            
            if not (root.val > left and root.val < right):
                return False
            
            k1 = traversal(root.left, left, root.val)
            k2 = traversal(root.right, root.val, right)
            return (k1 and k2)
            
            
        left = float("-inf") 
        right = float("+inf")
        return traversal(root, left, right)
        
