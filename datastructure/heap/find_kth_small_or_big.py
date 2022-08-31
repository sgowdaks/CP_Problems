----****#klog(k)****-------

#kth smallest
t=nums[:k]
h._heapify_max(t)
for i in range(k, len(nums)):
if t[0] > nums[i]:    
    h.heappop(t)
    h.heappush(t, arr[i])
return t[0]

#kth largest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        t=nums[:k]
        h.heapify(t)
        for i in range(k, len(nums)):
            if t[0]<nums[i]:    h.heappushpop(t, nums[i])
        return t[0]

    
    
-----**#nlog(n)***---------
#kth largest
class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        heapq._heapify_max(arr)   
        i = 0
        while i != k-1:
            heapq._heappop_max(arr)
            i = i + 1
            
        return heapq._heappop_max(arr)

#kth smallest
from heapq import heapify, heappush, heappop

class Solution:
    def kthSmallest(self,arr, l, r, k):
        heapify(arr)
        
        i = 0
        
        while i != k - 1:
            heappop(arr)
            i = i + 1
            
        return heappop(arr)
