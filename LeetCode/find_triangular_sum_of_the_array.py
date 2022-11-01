class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        new_arr = []
        while True:
            if len(nums) == 1:
                return nums[0]
            for i in range(0, len(nums)-1):
                sum_ = (nums[i]+nums[i+1]) % 10
                new_arr.append(sum_)
            nums = new_arr
            new_arr = []
