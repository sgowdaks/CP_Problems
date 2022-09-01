class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recurse(root, max_):
            if root == None:
                return 0
            else:
                res = 0
                count = 0
                if root.left != None:
                    if root.left.val >= max_:
                        count = count + 1
                        res = count + recurse(root.left, root.left.val)
                    else:
                        res = count + recurse(root.left, max_)
                        
                count = 0
                if root.right != None:
                    if root.right.val >= max_:
                        count = count + 1
                        res += count + recurse(root.right, root.right.val )
                    else:
                        res += count + recurse(root.right, max_)
                return res
                    
                            
        
        count = recurse(root, max_ = root.val)
        if root.val != None:
            return count + 1
        else:
            return 0
        
