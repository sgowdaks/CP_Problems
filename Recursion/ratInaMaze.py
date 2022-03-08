class Solution:
    def findPath(self, m, n):
        row = n - 1
        col = n - 1
        i = 0
        j = 0
        count = []
        st = ""
        self.rat(row, col, i, j, m, n, count, st)
        return count
        
    
    def rat(self, row, col, i, j, m, n, count, st ):
        if i == row and j == col:
            # print(st)
            count.append(st)
            return 1
        if m[i][j] == 1:
            m[i][j] = - 1
            if i+1 <= row and m[i+1][j] == 1:
                if self.rat(row, col, i + 1, j, m, n, count, st + "D") == 1:
                      pass
            if i-1 >= 0 and m[i-1][j] == 1:
                if self.rat(row, col, i - 1, j, m, n, count, st+ "U") == 1:
                     pass
            if j+1 <= col and m[i][j+1] == 1:
                if self.rat(row, col, i , j + 1, m, n, count, st+"R") == 1:
                     pass
            if j-1 >= 0 and m[i][j-1] == 1:
                if self.rat(row, col, i , j - 1, m, n, count, st+"L") == 1:
                    pass
            m[i][j] = 1
            return 0
        if m[i][j] == -1 or m[i][j] == 0:
            return 0
            
        return 1
