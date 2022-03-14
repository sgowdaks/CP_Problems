class Solution(object):        
    def diffWaysToCompute(self, s):
        def check(a, b, e):
            if e == "+":
                return int(a)+int(b)
            elif e == "-":
                return int(a)-int(b)
            elif e == "*":
                return int(a)*int(b)
            
        
        def compute(s, exp, dicti):
            if len(s) == 1:
                return s
            if s in dicti:
                return dicti[s]
            results = []
            for i in range(len(s)):
                if s[i] in exp:
                    right = compute(s[:i], exp, dicti)
                    left = compute(s[i+1:],exp, dicti)
                    # print(right, left)
                    for j in right:
                        for k in left:
                            results.append(check(j, k, s[i]))
            dicti[s] = results
            return results
        
        dicti = {}
        exp = ["-", "+", "*"]
        k = compute(s, exp, dicti)
        return k

            

                    
