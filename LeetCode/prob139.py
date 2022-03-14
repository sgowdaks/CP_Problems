class Solution:
    def wordBreak(self, s: str, dicti: List[str]) -> bool:
        ndicti = {}
        return self.wordB(s, dicti, ndicti)
 
    
    def wordB(self, s, dicti, ndicti):
        if s in ndicti:
            return ndicti[s]
        if s in dicti:
            return True
        for i in range(len(s)):
            word = s[0:i]
            # print(word)
            if word in dicti and self.wordB(s[i:],dicti, ndicti):
                ndicti[s] = True
                return True
        
        ndicti[s] = False
        return False
        
