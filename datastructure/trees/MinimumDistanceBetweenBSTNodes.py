class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int
        arr = []
        def recurse(root):
            if root == None:
                return 0
            
            arr.append(root.val)
            recurse(root.left)
            recurse(root.right)
            

        recurse(root)
        arr = sorted(arr)
        start = arr[0]
        min_ = 100000
        for i in range(1, len(arr)):
            min_ = min(min_, arr[i]-start)
            start = arr[i]
        return min_
