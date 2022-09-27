def findPreSuc(root, pre, suc, key):
    #your code goes here
    
    def pre_(root, pre, suc, key):
        while root:
            pre[0] = root
            root = root.right
            
        
    def suc_(root, pre, suc, key):
        while root:
            suc[0] = root
            root = root.left
        
    def traverse(root, pre, suc, key):
        if root == None:
            return
        if root.key > key:
            pre[0] = root
            traverse(root.right, pre, suc, key)
        elif root.key < key:
            suc[0] = root
            traverse(root.left, pre, suc, key)
        elif root.key == key:
            if root.left:
                pre_(traverse(root.left, pre, suc, key))
            if root.right:
                suc_(traverse(root.right, pre, suc, key))
            
    
    traverse(root, pre, suc, key)
