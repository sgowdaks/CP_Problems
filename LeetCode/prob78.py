class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = 2 ** len(nums)
        list1 = []
        for i in range(n):
            list2 = []
            for j in range(0, len(nums)):
			#this checks for each number 
                if 1 << j & i:
                    list2.append(nums[j])
            list1.append(list2)
        return list1
