from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 1:
            return [1]
        list1 = []
        start = 0 
        list2 = []
        
        def findIndex(s, ch):
            max_ = 0
            for i in range(len(s)):
                if s[i] == ch:
                    max_ = i
            return max_
        
        list2.append(s[0])
        end = findIndex(s, s[0])
        if end == 0:
            list1.append(len(list2))
            list2 = []
        for i in range(1, len(s)):
            list2.append(s[i])
            k = findIndex(s, s[i])
            # print(s[i], k, end, i)
            if k > end:
                end = k
            elif i == end:
                list1.append(len(list2))
                list2 = []
                start = end
            if len(list2) == 1 and end == i and k == i:
                list1.append(1)
                list2 = []

        return list1
            
            
    
                    
            
                
                
            
            
        
