class Solution:
    def median(self, matrix, r, c):
    	mid_pos = ((r * c)+1) // 2
    	min_ = matrix[0][0]
    	max_ = matrix[0][c-1]
    	
    	row = 1
    	while row < r:
    	    if matrix[row][0] < min_:
    	        min_ = matrix[row][0]
    	    if matrix[row][c-1] > max_:
    	        max_ = matrix[row][c-1]
    	    row = row + 1
    	    
    	print(min_, max_)    
    	while min_ < max_:
    	    
    	    mid = min_ + (max_ - min_) // 2
    	    # check how many numbers are lesser than mid_
    	    m_count = 0
    	    for row in range(r):
    	        count = 0
    	        for col in range(c):
    	            if matrix[row][col] <= mid:
    	                count += 1
    	        m_count += count

    	   # print(m_count, mid_pos)
    	    if m_count < mid_pos:
    	        min_ = mid + 1
    	    else:
    	        max_ = mid 
    	   # print(min_, max_)

    	return min_
    	    
