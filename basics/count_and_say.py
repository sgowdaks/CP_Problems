class Solution:
    def countAndSay(self, n: int) -> str:
        def recurse(n):
            if n == 1:
                return "1"
            else:
                answer = list(recurse(n-1))
                count = 0
                res = ""
                for i in range(len(answer)):
                    count = count + 1
                    if i == (len(answer)-1) or answer[i] != answer[i+1]:
                        res = res + str(count)
                        res = res + str(answer[i])
                        count = 0
                return res
    
        
        return recurse(n)
        
