class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      #method 1 : recursion
        def recursion(root, p, q):
            if root == None:
                return None
            
            if root.val == p.val:
                return p
            if root.val == q.val:
                return q
            
            left = recursion(root.left, p, q)
            right = recursion(root.right, p, q)
            
            
            if left == None and right == None:
                return None
            elif left == None and right != None:
                return right
            elif left != None and right == None:
                return left
            elif left != None and right != None:
                return root
            
            return recursion(root, p, q)
        
        
        #method 2 : DFS
        def traversal(root, p, q, p_found, q_found, p_path, q_path, arr, dicti ):
            if root == None:
                return 
            
            dicti[root.val] = root
            if p_found == False:
                p_path += str(root.val) + " "
                if root.val == p.val:
                    arr.append(p_path)
                    p_found = True
             
            if q_found == False:
                q_path += str(root.val) + " "
                if root.val == q.val:
                    arr.append(q_path)
                    q_found = True
                
                        
            traversal(root.left, p, q,  p_found, q_found,  p_path, q_path, arr, dicti)
            traversal(root.right, p, q, p_found, q_found,  p_path, q_path, arr, dicti)
        
        p_found = False
        q_found = False 
        p_path = ""
        q_path = ""
        arr = []
        dicti = {}
        traversal(root, p, q, p_found, q_found,  p_path, q_path, arr, dicti)
        
        val1  = arr[0].split(" ")
        val1 = val1[0:len(val1)-1]
        
        val2  = arr[1].split(" ")
        val2 = val2[0:len(val2)-1]
        
        min_ = min(len(val1), len(val2))
        
        no = 0
        
        for i in range(min_):
            if val1[i] == val2[i]:
                no = int(val1[i])                
            else:       
                return dicti[no]
        return dicti[no]
                
            
            
