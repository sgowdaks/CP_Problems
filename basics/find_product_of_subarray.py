class Solution:
	def maxProduct(self,arr, n):
	    res = max(arr)
	    max_ = 1
	    min_ = 1
	    
	    for num in arr:
	       # print(num)
	        if num == 0:
	            max_ = 1
	            min_ = 1
	            continue
	        tmp = num * max_
	        max_ = max(num * max_, num * min_, num)
	        min_ = min(tmp , num * min_, num)
	       # print(max_,min_)
	       # print(num * max_, num*min_, num)
	        res = max(max_, res)
	            
	    return res
