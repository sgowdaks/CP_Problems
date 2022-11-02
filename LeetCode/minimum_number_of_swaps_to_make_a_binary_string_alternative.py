class Solution:
    def minSwaps(self, s: str) -> int:
        zero = 0
        one = 0
        for i in s:
            if i == "0":
                zero += 1
            else:
                one += 1
                
        def starts_with_one(s):
            arr = []
            for i in range(len(s)):
                if i % 2 == 0:
                    arr.append("1")
                else:
                    arr.append("0")
            count = 0
            for i in range(len(s)):
                if s[i] != arr[i]:
                    count += 1
            return count // 2
        
        def starts_with_zero(s):
            arr = []
            for i in range(len(s)):
                if i % 2 == 0:
                    arr.append("0")
                else:
                    arr.append("1")
                    
            count = 0
            for i in range(len(s)):
                if s[i] != arr[i]:
                    count += 1
            return count // 2
            
        
        if zero - one == 1:
            #It starts with zero and end with zero
            print("zero")
            return starts_with_zero(s)
        elif one - zero == 1:
            #it starts with one and ends with one
            return starts_with_one(s)
        elif zero == one:
            #either starts with one or zero
            return min(starts_with_one(s),starts_with_zero(s))
        else:
            #not possible
            return -1
