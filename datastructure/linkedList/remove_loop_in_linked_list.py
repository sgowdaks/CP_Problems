class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        #floyd's algotithm
        slow = head
        fast = head
        
        while fast and fast.next and slow:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    break
            
            
        if slow == head:
            while fast.next != slow:
                fast = fast.next
            fast.next = None
        elif slow == fast:
            slow = head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
            fast.next = None
            
        return 1
