class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root == None:
            return []
        queue = []
        sum_ = []
        queue.append(root)
        while len(queue) > 0:
            val = 0      
            n = len(queue)
            for i in range(n):
                k = queue.pop(0)
                val += k.val
                if k.right:
                    queue.append(k.right)
                if k.left:
                    queue.append(k.left)
            ave = val / n
            sum_.append(ave)
        return sum_
        
