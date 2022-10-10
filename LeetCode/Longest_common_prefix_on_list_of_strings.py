class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first = strs[0]
        second = strs[-1]
        res = ""
        for i in range(len(first)):
            if first[i] != second[i]:
                return res
            res += first[i]
        return res
