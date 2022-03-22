class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        chars = ["a"] * n
        k = k - len(chars)
        i = len(chars) - 1
        while k > 0:
            if k > 25:
                chars[i] = chr(ord(chars[i])+25)
                k = k - 25
            else:
                chars[i] = chr(ord(chars[i])+k)
                k = 0
            i = i - 1
            # print(k, i)
        return "".join(chars)
