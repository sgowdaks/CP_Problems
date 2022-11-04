class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        max_i = 0
        max_ = max(nums)
        min_i = 0
        min_ = min(nums)
        
        #check for max_index towrads right
        for i in range(len(nums)):
            if nums[i] == max_:
                max_i = i
                
        #check for min_index towards left
        for i in reversed(range(len(nums))):
            if nums[i] == min_:
                min_i = i
                
        swaps = 0
        #if min_id more towards right
        if min_i > max_i:
            #overlapping so, start with min_element 
            swaps += min_i
            swaps += (len(nums)-max_i-1-1)
            
        #if max_id more towards right
        elif max_i > min_i:
            #they are not overlpping
            swaps += min_i
            swaps += len(nums) - max_i -1
            
        return swaps   
