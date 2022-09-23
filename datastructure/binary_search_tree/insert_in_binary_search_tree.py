def insert(root, key):
    # code here
    def traverse(root, key):
        if key == root.data:
            return
        if key < root.data:
            if root.left == None:
                root.left = Node(key)
                return
            else:
                traverse(root.left, key)
        else:
            if root.right == None:
                root.right = Node(key)
                return
            else:
                traverse(root.right, key)
            
        
    if root == None:
        return None
    traverse(root, key)
    return root
