class Solution:
    def divide(self, N, head):
        # root = head
        # low = head
        # high = head
        # while high != None:
        #     if high.data % 2 == 0:
        #         if high.data == low.data:
        #             high = high.next
        #             low = low.next
        #         else:
        #             tmp = low.data
        #             low.data = high.data
        #             t_root = low.next
        #             while t_root.data != low.data:
        #                 tmp_ = t_root.data
        #                 t_root.data = tmp
        #                 tmp = tmp_
        #                 t_root = t_root.next
        #             t_root.data = tmp
        #             low = low.next
        #             high = high.next

        #     else:
        #         high = high.next
        # return root
        
        even = None
        odd = None
        odd_ = None
        even_ = None
        root = head
        
        
        while head != None:
            if head.data % 2 == 0:
                if even == None:
                    even = head
                    even_ = even
                else:
                    even.next = head
                    even = head
            elif head.data % 2 != 0:
                if odd == None:
                    odd = head
                    odd_ = odd
                else:
                    odd.next = head
                    odd = head
            head = head.next
                    

        if even == None:
            return odd_
        even.next = odd_
        if odd_ != None:
            odd.next = None
    
        return even_
        
