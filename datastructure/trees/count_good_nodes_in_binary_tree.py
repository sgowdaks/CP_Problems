def goodNodes(self, root: TreeNode) -> int:
        def recurse(root, max_):
            if root == None:
                return 0
            else:
                res = 0
                if root.left != None:
                    if root.left.val >= max_:
						#will change the max_ value if greater than previous in left tree
                        res = 1 + recurse(root.left, root.left.val)
                    else:
                        res = recurse(root.left, max_)
                        
                if root.right != None:
                    if root.right.val >= max_:
						#will change the max_ value if greater than previous in right tree
                        res += 1 + recurse(root.right, root.right.val )
                    else:
                        res += recurse(root.right, max_)
                return res
                    
                            
        
        if root == None:
            return 0
        else:
            return (recurse(root, max_ = root.val) + 1)
