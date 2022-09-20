class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dicti = {}
        self.max_ = 1
        def findMax(root):
            if root == None:
                return 0
            if root.right == None and root.left == None:
                if root.val not in dicti:
                    dicti[root.val] = 1
                else:
                    dicti[root.val] += 1
                    self.max_ = max(dicti[root.val], self.max_)
                return root.val
            sum_ = root.val + findMax(root.left) + findMax(root.right)
            if sum_ not in dicti:
                dicti[sum_] = 1
            else:
                dicti[sum_] += 1
                self.max_ = max(dicti[sum_], self.max_)
            return sum_
        
        
        findMax(root)
        list1 = []
        
        for i in dicti.keys():
            if dicti[i] == self.max_:
                list1.append(i)
        return list1
            
