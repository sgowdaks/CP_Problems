class Solution:
	def lps(self, s):
		#computer LPS
		n = len(s)
		arr = [0] * n
		prev_val, cur = 0, 1
		
	    while cur < n:
	        if s[cur] == s[prev_val]:
	            arr[cur] = prev_val + 1
                cur += 1
		        prev_val +=1
		    else:
		        if prev_val == 0:
		            arr[cur] = 0
		            cur += 1
		        else:
		            prev_val = arr[prev_val-1]
		            
	    return arr[-1]
