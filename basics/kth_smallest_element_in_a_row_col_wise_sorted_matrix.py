#User function Template for python3

def kthSmallest(mat, n, k): 
    # Your code goes here
    min_ = mat[0][0]
    max_ = mat[n-1][n-1]
    while min_ < max_:
        mid = min_ + (max_ - min_) // 2
        count = 0
        for i in range(n):
            for j in range(n):
                if mat[i][j] <= mid:
                    count += 1
        
        # print(min_, max_,mid, count)
        if count < k:
            min_ = mid + 1
        else:
            max_ = mid
            
            
    
    return min_
            
            
          
