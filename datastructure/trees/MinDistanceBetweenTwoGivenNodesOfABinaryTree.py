class Solution:
    def findDist(self,root,a,b):
    
        #return: minimum distance between a and b in a tree with given root
        #code here
        
        def traverse(lca, a):
            if lca == None:
                return 0
                
            if lca.data == a:
                return 1
                
            left = traverse(lca.left, a)
            right = traverse(lca.right, a)
            # print(left, right)
            if right == 0 and left == 0:
                return 0
            else:
                return right + left + 1
            
        
        def recurse(root, a, b):
            
            if root == None:
                return None
            
            if root.data == a:
                return root
            if root.data == b:
                return root
                
            
            left = recurse(root.left, a, b)
            right = recurse(root.right, a, b)
            
            if left == None and right == None:
                return None
            elif left == None and right != None:
                return right
            elif right == None and left != None:
                return left
            else:
                return root
        
            
        lca = recurse(root, a, b)
        a_distance = traverse(lca, a)
        b_distance = traverse(lca, b)

        # print(a_distance, b_distance)
        return a_distance + b_distance  - 2
        
        
