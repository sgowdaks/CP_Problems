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
