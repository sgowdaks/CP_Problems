class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dicti = {}
        for i in arr:
            if i not in dicti:
                dicti[i] = 1
            else:
                dicti[i] += 1
        
        #sort the dicti based on values
        dicti = {h: v for h, v in sorted(dicti.items(), key=lambda item: item[1])}
        count = 0
        for key in dicti.keys():
            if dicti[key] <= k:
                k -= dicti[key]
            elif dicti[key] > k:
                count += 1
        return count
