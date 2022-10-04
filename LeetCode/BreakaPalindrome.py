class Solution:
    def breakPalindrome(self, pal: str) -> str:
        pal = list(pal)
        if len(pal) == 1:
            return ""
        for i in range(len(pal)):
            if pal[i] != "a":
                tmp = pal[i]
                pal[i] = "a"
                if pal == pal[::-1]:
                    pal[i] = tmp
                else:
                    return "".join(pal)
                
        pal[-1] = "b"
        return "".join(pal)
