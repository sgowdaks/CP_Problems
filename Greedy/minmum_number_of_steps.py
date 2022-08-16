class Solution:
	def minJumps(self, arr, n):
	   # jumps_arr = n * [0]
	   # if len(arr) == 1:
	   #     return 0
	   # jumps_arr[0] = 0
	   # if arr[0] == 0:
	   #     return -1
	   # for i in range(1, n):
	   #     for j in range(i):
	   #         distance = i - j
	   #         if arr[j] >= distance:
	   #             steps = jumps_arr[j] + 1
	   #             if jumps_arr[i] > steps:
	   #                 jumps_arr[i] = steps
	   #             elif jumps_arr[i] == 0:
	   #                 jumps_arr[i]= steps
	                    
	   # if jumps_arr[len(arr) - 1] == 0:
	   #     return -1
	        
	   # return jumps_arr[len(arr) - 1]
	                    
	                    
	   left = right = 0
	   steps = 0
	   distance = arr[0]
	   
	   while right < len(arr) - 1:
	       distance = 0
	       for i in range(left, right+1):
	           distance = max(distance, i + arr[i])
	       left = right + 1
	       right = distance
	       steps +=  1
	       if right == 0:
	           return -1
	           
