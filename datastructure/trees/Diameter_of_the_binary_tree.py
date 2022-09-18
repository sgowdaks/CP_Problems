class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      if root == None:
        return 0
      
      self.max_ = 0
      
      def binarytree(root):
        if root == None:
          return 0
        
        lefth = binarytree(root.left)
        righth = binarytree(root.right)
        
        self.max_ = max(lefth + righth + 1, self.max_)
        
        return max(lefth + righth) + 1
      
      binarytree(root)
      return self.max_ + 1
        
        
        
        
