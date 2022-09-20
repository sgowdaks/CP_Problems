class Solution:
	def setBits(self, N):
		# code here
		binary = bin(N)
		count = 0
		for i in binary[2:]:
		    if i == "1":
		        count += 1
		return count
