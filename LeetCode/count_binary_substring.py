class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 1
        n = len(s)
        cur = 1
        prev = 0
        sum_ = 0
        
        while i < n:
            if s[i] == s[i-1]:
                cur += 1
            elif s[i] != s[i-1]:
                sum_ += min(cur, prev)
                prev, cur = cur, prev
                cur = 1
            i += 1
        
        sum_ += min(prev, cur)
        return sum_
                
