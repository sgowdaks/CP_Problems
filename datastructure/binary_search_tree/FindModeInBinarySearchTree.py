class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dicti = {}
        
        def mode_(root, dicti, max_):
            if root == None:
                return max_
            
            if root.val not in dicti:
                dicti[root.val] = 1
            else:
                dicti[root.val] += 1
            max_ = max(max_, dicti[root.val])
            
            return max( mode_(root.left, dicti, max_), mode_(root.right,  dicti, max_), max_ )
        
        max_ = 0
        m = mode_(root, dicti, max_ )
        list1 = []
        for i in dicti.keys():
            if dicti[i] == m:
                list1.append(i)
        
        return list1
