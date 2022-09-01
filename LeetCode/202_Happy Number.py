class Solution:
    def isHappy(self, n: int) -> bool:
        def recurse(n, s):
            if n == 1:
                return 1
            else:
                count = 0
                while n > 0:
                    reminder = n % 10
                    count += reminder * reminder
                    n = n // 10
                if count in s:
                    return False
                s.add(count)
                if recurse(count, s) == True:
                    return True
        
        s = set()
        return recurse(n,s)

            
        
