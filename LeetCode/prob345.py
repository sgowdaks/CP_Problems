class Solution:
    def reverseVowels(self, s: str) -> str:
        list1 = ("a", "e", "i", "o", "u", "A", "E", "I","O", "U")
        left = 0
        s = list(s)
        right = len(s) - 1
        while left < right:
            if s[left] not in list1:
                left = left + 1
            elif s[right] not in list1:
                right = right - 1
            else:
                s[left], s[right] = s[right], s[left]
                left = left + 1
                right = right - 1
        return "".join(s)
