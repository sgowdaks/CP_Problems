class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goals = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= goals:
                print(nums[i], nums[i]+i, goals)
                goals = i
        
        if goals == 0:
            return True
        else:
            return False

        
#         if len(nums) == 1:
#             return True
#         if nums[0] == 0:
#             return False
        
#         l = 0
#         r = 0
        
#         while r < len(nums) - 1:
#             new_ = 0
#             # print(l, r)
#             for i in range(l,r+1):
#                 new_ = max(new_, i + nums[i])
#             if new_ == r:
#                 return False
#             l = r + 1
#             r = new_
#             # print(l, r)
#             if r >= len(nums) - 1:
#                 return True
