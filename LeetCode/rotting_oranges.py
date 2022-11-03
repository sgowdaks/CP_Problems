class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        good_oranges = 0
        rotten_oranges = 0
        rotten = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good_oranges += 1
                elif grid[i][j] == 2:
                    rotten_oranges += 1
                    rotten.append([i, j])
                    
        if good_oranges == 0 and rotten_oranges == 0:
            return 0
                    
        r = len(grid)
        c = len(grid[0])
        
        count = -1
        
        while len(rotten) > 0:
            count += 1
            l = len(rotten)
            for i in range(l):
                row, col = rotten.pop(0)
                # print(row, col)
                if row+1 < r and col < c and grid[row+1][col] == 1:
                    # print("first")
                    rotten.append([row+1,col])
                    grid[row+1][col] = 2
                    good_oranges -= 1
                    rotten_oranges += 1

                if row-1 >= 0 and col < c and grid[row-1][col] == 1:
                    # print("second")
                    rotten.append([row-1,col])
                    grid[row-1][col] = 2
                    good_oranges -= 1
                    rotten_oranges += 1

                if col+1 < c and row < r and grid[row][col+1] == 1:
                    # print("third")
                    rotten.append([row, col+1])
                    grid[row][col+1] = 2
                    good_oranges -= 1
                    rotten_oranges += 1

                if col-1 >= 0 and row < r and grid[row][col-1] == 1:
                    # print("fourth")
                    rotten.append([row, col-1])
                    grid[row][col-1] = 2
                    good_oranges -= 1
                    rotten_oranges += 1
                    
            # print(rotten)

        
        if good_oranges == 0:
            return count 
        return -1
                
        
        
