class Solution:	
	def search(self,pat, txt):
	    pat = list(pat)
	    txt = list(txt)
	    
	    list1 = [0] * 26
	    list2 = [0] * 26
	    for i in range(len(pat)):
	        list1[ord(pat[i]) - 97] += 1
	        list2[ord(txt[i]) - 97] += 1
	
    	count = 0
    	start = 0
    	end = len(pat) 
    	
    	while end < len(txt):
    	    if list1 == list2:
    	        count += 1
    	    list2[ord(txt[start]) - 97] -= 1
    	    list2[ord(txt[end]) - 97] += 1
    	    start = start + 1
    	    end = end + 1
    	
    	if list1 == list2:
    	    return count + 1
    	else:
    	    return count
