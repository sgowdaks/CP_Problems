class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        k = -1
        prev = nums[len(nums)-1]
        for i in reversed(range(len(nums)-1)):
            if prev > nums[i]:
                k = i 
                break
            else:
                prev = nums[i]
        check_with = nums[i]
        # print(k)
        if k == -1:
            return nums.reverse()
        else:
            l = len(nums) - 1
            while k < l:
                if nums[l] > check_with:
                    break
                l = l - 1
            nums[l], nums[k] = nums[k], nums[l]
            l = len(nums) - 1
            k = k + 1
            while l > k:
                nums[l],nums[k] = nums[k],nums[l]
                l = l - 1
                k = k + 1
        
        
        
            
        
    
                
            
