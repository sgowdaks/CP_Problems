class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        
        def mergesort(head):
            #partician algorithm
            if head != None:
                if head.next == None:
                    return head
                
                def partision(head):
                    root = head
                    slow = head
                    fast = head.next
                    while fast != None and fast.next != None:
                        slow = slow.next
                        fast = fast.next.next
                    return slow, root
                        
                
                slow, root = partision(head)
                mid = slow.next
                slow.next = None
                
                left = mergesort(root)
                right = mergesort(mid)
                
                #merge 2 sorted array
                ma = None
                main = None
                while left != None and right != None:
                    if left.data <= right.data:
                        if ma == None:
                            ma = left
                            main = ma
                        else:
                            ma.next = left
                            ma = ma.next
                        left = left.next
                        
                    elif left.data > right.data:
                        if ma == None:
                            ma = right
                            main = ma
                        else:
                            ma.next = right
                            ma = ma.next
                        right = right.next
                
                if left == None:
                    while right != None:
                        ma.next = right
                        ma = ma.next
                        right = right.next
                elif right == None:
                    while left != None:
                        ma.next = left
                        ma = ma.next
                        left = left.next
                        
                return main
            else:
                return None
                    
                        
        return mergesort(head)            
