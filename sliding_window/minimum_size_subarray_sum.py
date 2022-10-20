class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_ = 0
        count = 0
        min_ = len(nums)
        start = 0
        end = 0
        flag = 0
        
        while end < len(nums):
            if nums[end] == target:
                return 1
            
            sum_ += nums[end]
            count += 1
            
            if sum_ >= target:
                flag = 1
                min_ = min(count , min_)
                while sum_ > target:
                    sum_ -= nums[start]
                    start += 1  
                    count -= 1
                    if sum_ >= target:
                        min_ = min(count , min_)

                
            end = end + 1
        
        if sum_ >= target:
            return min(min_, count)
        
        if flag == 0:
            return 0

        return min_
                
        
