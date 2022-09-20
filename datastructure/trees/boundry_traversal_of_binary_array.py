class Solution:
    def printBoundaryView(self, root):
        # Code here
        
        #left boundry
        answer = []
        def leftBoundry(root):
            if root == None:
                return
            if root.left:
                answer.append(root.data)
                leftBoundry(root.left)
            elif root. right:
                answer.append(root.data)
                leftBoundry(root.right)
                
                
        #get leaf nodes
        def leafNodes(root):
            if root == None:
                return 
            leafNodes(root.left)
            if root.left == None and root.right == None:
                answer.append(root.data)
            leafNodes(root.right)
            
        #get right boundry
        def rightBoundry(root, k):
            if root == None:
                return
            if root.right:
                k.append(root.data)
                rightBoundry(root.right, k)
            elif root.left:
                k.append(root.data)
                rightBoundry(root.left, k)
            
                
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.data]
            
        answer.append(root.data)
        
        leftBoundry(root.left)
        leafNodes(root)
        k = []
        rightBoundry(root.right, k)
        # print(k)
        for i in k[::-1]:
            answer.append(i)
            
        return answer
            
