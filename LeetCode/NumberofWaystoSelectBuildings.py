class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = 0
        ones = 0
        for i in s:
            if i == "1":
                ones += 1
            else:
                zeros += 1
        
        ans = 0
        z, o = 0, 0
        
        for i in s:
            if i == "0":
                ans += o * (ones-o)
                z += 1
            else:
                ans += z * (zeros - z)
                
                o += 1
                
        return ans
