class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        i = 0 
        j = n 
        while j <= h:
            if haystack[i:j] == needle:
                return i
            i = i + 1
            j = j + 1
        return -1
            
        
        
