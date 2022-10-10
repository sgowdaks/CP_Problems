class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s = list(s)
        t = list(t)
        dicti = {}
    
        for i in range(len(s)):
            if s[i] not in dicti:
                
                if t[i] in dicti.values():
                    return False
                
                dicti[s[i]] = t[i]
                
            elif dicti[s[i]] != t[i]:
                    return False
        
        return True
