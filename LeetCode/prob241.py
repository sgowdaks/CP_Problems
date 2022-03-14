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
            if "+" not in s and "-" not in s and "*" not in s:
                # print(s)
                # print("hello")
                return [s]
            if s in dicti:
                return dicti[s]
            results = []
            for i in range(len(s)):
                if s[i] in exp:
                    # print(len(s[:i]),len(s[i+1:]))
                    right = compute(s[:i], exp, dicti)
                    # print(right)
                    left = compute(s[i+1:],exp, dicti)
                    # print(left)
                    # print(right, left)
                    for j in right:
                        for k in left:
                            results.append(check(j, k, s[i]))
                            # print(results)
            dicti[s] = results
            return dicti[s]
        
        dicti = {}
        exp = ["-", "+", "*"]
        k = compute(s, exp, dicti)
        # print(k)
        if len(k) == 0:
            list1 = []
            list1.append(int(s))
            return list1
        else:
            return k

            

                    
                
                        
                        
                
