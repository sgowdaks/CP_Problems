class Solution:
    def reverseBetween(self, head: Optional[ListNode], start: int, end: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        if start == end:
            return head
        
        m_root = head
        
        count = 1
        prev_ = None
        
        while head != None and count < start:
            prev_ = head
            head = head.next
            count += 1
        
        root = head.next
        prev = head
        head.next = None
        curr = root
            
        while curr != None and count < end:
            tmp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = tmp 
            count = count + 1
        
        if prev_ != None:
            tmp = prev_.next
            prev_.next = prev
            tmp.next = curr
            return m_root
        else:
            m_root.next = curr
            return prev
            
            
