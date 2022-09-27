class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dicti = {"2": "abc", "3": "def", "4": "ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        digit = list(digits)
        
        
        def recurse(st, num, list1):
            if len(st) == len(digit):
                list1.append(st)
            else:
                for i in dicti[digit[num]]:
                    recurse(st + i,num+1, list1)
                
        if digits == "":
            return []
        list1 = []
        st = ""
        recurse(st, 0, list1)
        return list1
