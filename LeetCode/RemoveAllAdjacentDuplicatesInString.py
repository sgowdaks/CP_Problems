class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        n = len(s)
        stack = []
        num = 0
        
        while num < n:
            if len(stack) == 0:
                stack.append(s.pop(0))
            elif s[0] == stack[-1]:
                stack.pop()
                s.pop(0)
            else:
                stack.append(s.pop(0))
            num += 1
            
        return "".join(stack)
