def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,k in enumerate(nums):
            #print(i,k)
            l = target - k
            if l in nums:
                if nums.index(l) != i :
                    return i, nums.index(l)
