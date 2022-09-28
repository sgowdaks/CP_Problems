class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = head
        fast = head.next        
        while fast and fast.next != None and slow != None:
            if slow != fast:
                slow = slow.next
                fast = fast.next.next
            else:
                return True
        return False
