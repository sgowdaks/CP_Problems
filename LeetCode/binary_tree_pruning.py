class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(root):
            if root == None:
                return None
            root.left = traversal(root.left)
            root.right = traversal(root.right)
            if root.left == None and root.right == None:
                if root.val == 0:
                    return None
                else:
                    return root
            else:
                return root
        
        return traversal(root)
