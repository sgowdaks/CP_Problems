class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s = list(s)
        
        string = []
        count = []
        
        
        for i in range(0, len(s)):
            if len(string) == 0:
                string.append(s[i])
                count.append(1)               
            elif s[i] == string[-1]:
                count[-1] += 1
                
                if count[-1] == k:
                    string.pop()
                    count.pop()
            else:
                    string.append(s[i])
                    count.append(1)
            
        st = ""
        
        
        for i in range(len(count)):
            st += string[i] * count[i]
            
        return st
        
