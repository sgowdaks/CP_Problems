class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        newst = ""
        s = list(s)
        spaces = set(spaces)
        for i, val in enumerate(s):
            if i in spaces:
                newst += " "
                j = j + 1
            newst += val

        
        return newst
