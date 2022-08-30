mat = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
     
#transpose
for i in range(0, len(mat)):
    for j in range(i, len(mat)):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        
#clock-wise

for i in range(0, len(mat)):
    left = 0
    right = len(mat) - 1
    while left < right:
        mat[i][left], mat[i][right] = mat[i][right], mat[i][left]
        left = left + 1
        right = right - 1
        
#anti clock-wise

for i in range(0, len(mat)):
    top = 0
    down = len(mat) - 1 
    while top < down:
        mat[top][i], mat[down][i] = mat[i][top], mat[i][down]
        top = top + 1
        down = down - 1

for i in range(len(mat)):
    print(mat[i])
        
        
    
        
