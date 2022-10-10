class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        #prefix sum method
        arr = []
        net = 0
        for i in nums:
            net += i
            arr.append(net)
        
        min_ = min(arr)
        if min_ < 0:
            return abs(min_) + 1
        else:
            return 1            
        
        
#         min_ = min(nums)
#         if min_ >= 0:
#             return 1
#         net_sum = 0
        
#         def call(nums, net_sum):
#             for num in nums:
#                 net_sum = net_sum + num
#                 if net_sum < 1:
#                     return True
#             return False
        
#         k = True
#         while k:
#             net_sum += 1
#             k = call(nums, net_sum)
            
#         return net_sum 
