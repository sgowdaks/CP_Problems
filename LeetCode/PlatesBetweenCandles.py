class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        def calcualte_stars(start, end, cu_sum):
            if end - start == 1 or start == end or start - end == 1:
                return 0
            else:
                # print(start ,end)
                count = 0
                s , e = min(start, end), max(start, end)
                count = cu_sum[e] - cu_sum[s]
            return count
            
                
            
        
        right = [len(s)] * len(s)
        left = [-1] * len(s)
        
        change = -1
        for i in range(len(left)):
            if s[i] == "|":
                change = i
                left[i] = change
            else:
                left[i] = change
        
        change = len(s)
        for i in reversed(range(len(right))):
            if s[i] == "|":
                change = i
                right[i] = change
            else:
                right[i] = change
                
        cu_sum = []
        sum_ = 0
        for i in range(len(left)):
            if s[i] == "*":
                sum_ = sum_ + 1
            cu_sum.append(sum_)

                
        result = []
        for query in queries:
            count = 0
            start = query[0]
            end = query[1]
            #cond1: both are equal
            if start == left[start] and end == right[end]:
                count += calcualte_stars(start, end, cu_sum)
            elif left[start] <= start and left[end] <= end:
                if start <= left[end] and end >= right[start]: 
                    count += calcualte_stars(left[end], right[start], cu_sum)
            
            result.append(count)
        return result
                
                
            

                
                
                
            
        
        
    
        
