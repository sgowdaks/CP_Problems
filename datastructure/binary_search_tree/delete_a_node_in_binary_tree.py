class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            if root:
                if root.val > key:
                    root.left = self.deleteNode(root.left,key)

                elif root.val < key:

                    root.right = self.deleteNode(root.right,key)
                else:
                    if root.left == None and root.right == None:
                        return None
                    if root.left == None or root.right == None:
                        if root.left:
                            return root.left
                        else:
                            return root.right

                    else:
                        #By using inorder predecessor
                        temp = root.left
                        while temp.right !=None:
                            temp=temp.right
                        root.val=temp.val

                        root.left = self.deleteNode(root.left,temp.val)

            return root
                
            
