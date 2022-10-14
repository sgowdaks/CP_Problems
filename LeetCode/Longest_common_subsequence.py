class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = list(text1)
        text2 = list(text2)
        
        n = len(text1) - 1
        m = len(text2) - 1
        
        count = 0
        
        def recurse(text1, text2, n , m, dp ):
            if n < 0 or m < 0:
                return 0
            else:
                if (n, m) in dp:
                    return dp[(n, m)]
                
                if text1[n] == text2[m]:
                    val1 = recurse(text1, text2, n-1 , m-1, dp) + 1 
                    dp[tuple([n, m])] = val1
                    return val1
                else:  
                    val2 = max(recurse(text1, text2, n - 1 , m, dp) , recurse(text1, text2, n , m-1, dp))
                    dp[tuple([n, m])] = val2
                    return val2
                
        dp = {}   
        return recurse(text1, text2, n , m, dp)
            
