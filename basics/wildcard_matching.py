class Solution:
  #not an optimized solution, and hence you will get TLE error
    def isMatch(self, s: str, p: str) -> bool:        
        s = list(s)
        p = list(p)
        
        i = 0
        j = 0
        
        def startFunction(i, j):
            if i == len(s) and j == len(p):
                return True
            
            elif i == len(s)  and j != len(p)  and p[j] == '*':
                return startFunction(i, j + 1)
            
            elif i == len(s)  or j == len(p):
                    return False                
                
            if s[i] == p[j] or p[j] == "?":
                return startFunction(i + 1, j + 1)  
            elif p[j] == "*":
                k = (startFunction(i, j + 1) or startFunction(i+1, j))
                return k
            else:
                return False
            
        return startFunction(i, j)
