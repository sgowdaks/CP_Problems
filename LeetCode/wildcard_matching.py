class Solution:
    def isMatch(self, s: str, p: str) -> bool:        
        s = list(s)
        p = list(p)
        
        i = len(s)-1
        j = len(p)-1 
        
        def startFunction(i, j, dp):
            if (i,j) in dp:
                return dp[(i, j)]
            
            if i < 0 and j < 0:
                return True            
            elif i < 0 and j >= 0   and p[j] == '*':
                k = startFunction(i, j - 1, dp)
                dp[tuple([i, j])] = k
                return k
            
            elif i < 0  or j < 0:
                    return False                
                
            if s[i] == p[j] or p[j] == "?":
                k = startFunction(i - 1, j - 1, dp)  
                dp[tuple([i, j])] = k
                return k
            
            elif p[j] == "*":
                k = (startFunction(i, j - 1, dp) or startFunction(i-1, j, dp))
                dp[tuple([i, j])] = k
                return k
            
            else:
                dp[tuple([i, j])] = False
                return False
        
        dp = {}
        return startFunction(i, j, dp)
        
 
    
                
