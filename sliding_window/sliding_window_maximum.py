class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return max(nums)
        arr  = []
        queue = []
        for i in range(k):
            while len(queue) > 0 and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
            
        print(queue)
                
        end = k 
        start = 0
        while end < len(nums):
            arr.append(queue[0])
            
            if queue[0] == nums[start]:
                queue.pop(0)
                
            if len(queue) > 0:                
                while len(queue) > 0 and nums[end] > queue[-1]:
                    queue.pop()
                    
            queue.append(nums[end])
            start += 1
            end += 1
        
        arr.append(queue[0])
        return arr
