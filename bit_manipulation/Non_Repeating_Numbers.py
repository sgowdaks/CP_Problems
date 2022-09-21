class Solution:
	def singleNumber(self, nums):
		# Code here
		XOR =  nums[0]
		#Xor everything (to get every number cancelled out)
		for i in range(1, len(nums)):
		    XOR = XOR ^ nums[i]
		    
		#find right most significant bit
		XOR = XOR & ~(XOR - 1)
		
		#divide it into category
		x = y = 0
		for i in range(len(nums)):
		    if XOR & nums[i]:
		        x = x ^ nums[i]
		    else:
		        y = y ^ nums[i]
# 	print(x, y)
		if x > y:
		    return [y, x]
		else:
		    return [x, y]
