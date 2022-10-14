class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        s = list(s)
        net = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "[":
                net += 1
            elif s[i] == "]":
                net -= 1
            
            if net < 0:
                count = min(count, net)
        
        k = (abs(count) + 1) // 2;
        return k
