class Solution:
	def setBits(self, N):
		# code here
		#method 1
		count = 0
		while N > 0:
		    if N & 1 == 1:
		        count += 1
		    N = N >> 1
		return count
		
		
		
		#method 2
		def recurse(N):
		    if N == 0:
		        return 0
		    if N % 2 == 0:
		        N = N // 2
		        return recurse(N)
		    else:
		        N = N // 2
		        return 1 + recurse(N)
		    
		    
		return recurse(N)
		
		#method 3
		binary = bin(N)
		count = 0
		for i in binary[2:]:
		    if i == "1":
		        count += 1
		return count
