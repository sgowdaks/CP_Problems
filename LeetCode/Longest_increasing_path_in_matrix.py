class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        def recurse(i, j, memo, val):
            if i < 0 or i == n or j == m or j < 0 or matrix[i][j] <= val:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 1
            res = max(res, 1 + recurse(i+1, j, memo,  matrix[i][j]))
            res = max(res, 1 + recurse(i-1, j, memo,  matrix[i][j]))
            res = max(res, 1 + recurse(i, j-1, memo, matrix[i][j]))
            res = max(res, 1 + recurse(i, j+1, memo, matrix[i][j]))
                    
            memo[(i ,j)] = res
                
            return res

            
        # return 1 + recurse(0, 0,  matrix[0][0])
        
        memo = {}
        max_ = 0
        for i in range(n):
            for j in range(m):
                max_ = max(max_, recurse(i, j, memo,   -1))
                # print(max_)
        return max_
