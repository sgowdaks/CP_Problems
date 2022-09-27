class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        succ = None
        
        def traverse(root, succ, p):
            if root == None:
                return succ

            if p.val > root.val:
                return traverse(root.right, succ, p)
            elif p.val < root.val:
                succ = root
                return traverse(root.left, succ, p)
            else:
                if root.right != None:
                    return traverse(root.right, succ, p)
                    
                return succ
        
        return traverse(root, succ, p)
