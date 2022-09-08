# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:        
        def traversal(dicti, root, row, col, max_, min_):
            if root == None:
                return None
            else:
                if row in dicti:
                    dicti[row].append([col, root.val])
                    # print(dicti[row])
                else:
                    dicti[row] = [[col, root.val]]
                    # print(dicti[row])
                    
                traversal(dicti, root.left, row - 1, col + 1, max_, min_)
                traversal(dicti, root.right, row + 1, col + 1, max_, min_)
                
        dicti = {}
        row = 0
        col = 0
        max_ = [0]
        min_ = [0]
        traversal(dicti, root, row, col, max_, min_)
        list1 = []
        for i in sorted(dicti.keys()):
            co = sorted(dicti[i], key = lambda x:(x[0], x[1]))
            col_sorted = []
            for p in co:
                col_sorted.append(p[1])
            list1.append(col_sorted)
            
            
        return list1
            
            
                
        
