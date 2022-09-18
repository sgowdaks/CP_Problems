def findIntersection(head1,head2):
    list1 = []
    while head1 != None and head2!= None:
        if head1.data < head2.data:
            head1 = head1.next
        elif head2.data < head1.data:
            head2 = head2.next
        else:
            list1.append(head1.data)
            head1 = head1.next
            head2 = head2.next
    
    root = None 
    for i in list1:
        if root == None:
            root = Node(i)
            node = root
        else:
            node.next = Node(i)
            node = node.next
    
    return root
