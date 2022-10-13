class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s) 
        s = s + s
        s = [int(i) for i in s]
        list1 = [0] * (n*2)
        list2 = [0] * (n*2)
        
        for i in range(len(list1)):
            if i%2 == 0:
                list1[i] = 1
            else:
                list2[i] = 1
                
        # print(list1)
        # print(list2)
        
        def checkfor(i, n, list1, s):
            list1 = list1[i:n+i]
            count = 0
            for i in range(n):
                if list1[i] != s[i]:
                    count += 1
            return count
        
        min1 = n
        min2 = n
        min1 = min(min1, checkfor(0, n, list1, s))
        min2 = min(min2, checkfor(0, n, list2, s))
        
        
        # for i in range(n):
        #     min_ = min(checkfor(i, n, list1, s), min_)
        #     min_ = min(checkfor(i, n, list2, s), min_)
        #     k = s.pop(0)
        #     s.append(k)
        # print(min1, min2)
        
        main_min = min(min1, min2)
        
        n = n - 1
        for i in range(1, n+1):
            # print(i-1, n+i)
            if list1[i-1] != s[i-1]:
                min1 = min1 - 1
            if list1[n + i] != s[n+i]:
                min1 += 1
                
            if list2[i-1] != s[i-1]:
                min2 = min2 - 1
                
            if list2[n + i] != s[n+i]:
                min2 += 1
            
            main_min = min(main_min, min1, min2)   
            # print(main_min)
            
            
            
        return main_min
            
