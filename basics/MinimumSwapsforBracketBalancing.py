class Solution:
    def minimumNumberOfSwaps(self,S):
        # code here 
        
        net = 0
        s = list(S)
        open = 0
        close = 0
        net = 0
        swap = 0
        for i in range(len(s)):
            if s[i] == "[":
                if (close - open) > 0:
                    swap += (close - open)
                open += 1
            elif s[i] == "]":
                close += 1
                
        return swap
