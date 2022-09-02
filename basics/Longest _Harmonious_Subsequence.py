class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #method 1: By sorting
        dicti = {}
        for i in range(len(nums)):
            if nums[i] not in dicti:
                dicti[nums[i]] = 1
            else:
                dicti[nums[i]] += 1
        dicti = dict(sorted(dicti.items()))
        prev = min(nums)
        max_ = 0
        for i in dicti.keys():
            if prev == i:
                continue
            else:
                curr = i
                if curr - prev == 1:
                    count = dicti[curr] + dicti[prev]
                    max_ = max(max_, count)
                prev = curr
        return max_
        
        #method 2: without sorting
        
        dicti = {}
        
        for i in nums:
            if i in dicti:
                dicti[i] += 1
            else:
                dicti[i] = 1
         
        max_ = 0
        for i in dicti.keys():
            if i + 1 in dicti.keys():
                max_ = max(max_, dicti[i+1] + dicti[i])
            if i - 1 in dicti.keys():
                max_ = max(max_, dicti[i-1] + dicti[i])
        return max_
                
