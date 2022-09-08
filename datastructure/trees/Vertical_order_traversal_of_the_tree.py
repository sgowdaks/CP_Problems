class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:        
        def traversal(dicti, root, val):
            if root == None:
                return None
            else:
                if val in dicti:
                    dicti[val] = dicti[val] + [root.val]
                else:
                    dicti[val] = [root.val]
                #traversal(dicti, root.right, val + 1)
                traversal(dicti, root.left, val - 1)
                traversal(dicti, root.right, val + 1)
                
        dicti = {}
        val = 0
        traversal(dicti, root, val)
        list1 = []
        print(dicti)
        for i in sorted(dicti.keys()):
            list1.append(dicti[i])
        return list1
            
