#method 1
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB
        
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        
        return l1
    
#method2
def intersetPoint(head1,head2):
    one = 0
    two = 0
    l1 = head1
    l2 = head2
    while head1 != None:
        one += 1
        head1 = head1.next
    
    while head2 != None:
        two += 1
        head2 = head2.next
        
    if one > two:
        diff = one - two
        while diff > 0:
            l1 = l1.next
            diff -= 1
    elif two > one:
        diff = two - one
        while diff > 0:
            l2 = l2.next
            diff -= 1
    
    while l1 != l2:
        l1 = l1.next
        l2 = l2.next
    
    return l1.data
    

