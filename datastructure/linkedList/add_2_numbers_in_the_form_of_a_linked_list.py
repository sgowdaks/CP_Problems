class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        sum_ = 0
        st1 = ""
        st2 = ""
        while first != None:
            st1 = st1 + str(first.data)
            first = first.next
        
        while second != None:
            st2 = st2 + str(second.data)
            second = second.next
            
        # print(st1, st2)
        
        sum_ = int(st1) + int(st2)
        m = None
        sum_ = str(sum_)
        for i in sum_:
            # print(i)
            if m == None:
                m = Node(int(i))
                root = m 
            else:
                root.next = Node(int(i))
                root = root.next
        
        return m  
    
    
    
    # root1 = None
    # root2 = None
    # def addTwoLists(self, first, second):
    #     #reverse the linked list
    #     def reverse(first):
    #         curr = first.next
    #         prev = None
    #         while first.next != None:
    #             k = first.next
    #             first.next = prev
    #             prev = first
    #             first = k
            
    #         first.next = prev
    #         return first
        
    #     root1 = reverse(first)
    #     root2 = reverse(second)
        
        
    #     sum_ = ""
    #     reminder = 0
    #     while root1 != None and root2 != None:
    #         val = root1.data + root2.data + reminder
    #         reminder = val // 10
    #         val = val % 10
    #         sum_ = str(val) + sum_
    #         root1 = root1.next
    #         root2 = root2.next
    #         # print(sum_)
        
    #     if root1 != None:
    #         while root1 != None:
    #             val = root1.data + reminder
    #             reminder = val // 10
    #             val = val % 10
    #             sum_ = str(val) + sum_
    #             root = root1.next
        
    #         sum_ += str(reminder)
        
    #     if root2 != None:
    #         while root2 != None:
    #             val = root2.data + reminder
    #             reminder = val // 10
    #             val = val % 10
    #             sum_  = str(val) + sum_
    #             root2 = root2.next
        
    #         sum_ =  str(reminder) + sum_
        
    #     sum_ = int(sum_)
    #     sum_ = str(sum_)
    #     # print(sum_)
    #     m = None
    #     for i in sum_:
    #         # print(i)
    #         if m == None:
    #             m = Node(int(i))
    #             root = m 
    #         else:
    #             root.next = Node(int(i))
    #             root = root.next
        
    #     return m  
        
            
        
