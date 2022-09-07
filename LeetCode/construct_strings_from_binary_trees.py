class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def traversal(root):
            if root == None:
                return None
            else:
                k_l = traversal(root.left)
                k_r = traversal(root.right)
                if k_l == None and k_r == None:
                    return "(" + str(root.val) + ")"
                elif k_l == None:
                    return "("+ str(root.val) + "()" + k_r + ")"
                elif k_r == None:
                    return "("  + str(root.val) + k_l + ")"
                elif root.left and root.right:
                    return "(" + str(root.val) + k_l + k_r + ")"
    
                
        st = traversal(root)
        if root == None:
            return ""
        elif root.left == None and root.right == None:
            return str(root.val)
        list1 = list(st)
        list1.pop(0)
        list1.pop(-1)
        return "".join(list1)
        
