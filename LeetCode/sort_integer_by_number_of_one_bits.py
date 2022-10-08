from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        dicti = defaultdict(list)
        for num1 in arr:
            count = bin(num1).count("1")
            # count = 0
            # num = num1
            # while num > 0:
            #     if num == 1 or num == 2:
            #         count += 1
            #         break
            #     k = num % 2
            #     if k == 1:
            #         count +=  1
            #     num = num // 2
            dicti[count].append(num1)
            
        new_ = []
        dicti = dict(sorted(dicti.items()))
        for i in dicti.values():
            for j in i:
                new_.append(j)
        return new_
