class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_ = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # print(i,j)
                    k = self.search_area(i, j, grid) 
                    if k > max_:
                        max_ = k
        return max_
    
    def search_area(self, i, j, grid):
        # print(i,j)
        m = len(grid)
        n = len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] <= 0 :
            # print("hello")
            return 0 
        
        grid[i][j] = -1
        right = self.search_area(i,j+1, grid)
        left = self.search_area(i,j-1, grid)
        up = self.search_area(i-1,j, grid)
        down = self.search_area(i+1,j, grid)
        total_area = right + left + up + down + 1  
        return total_area
