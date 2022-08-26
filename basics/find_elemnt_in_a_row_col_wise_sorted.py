mat = [[10, 20, 30, 90],
        [15, 25, 35, 95],
        [27, 29, 39, 100],
        [32, 33, 39, 101]]
        
key = 33
    
row = len(mat)
col = len(mat[0])


def find_key(r, c, mat, row, col):
    while r < row and r >= 0 and c < col and c >= 0:
        print(r, c)
        if mat[r][c] == key:
            return True
        elif mat[r][c] > key:
            c = c - 1
        elif mat[r][c] < key:
            r = r + 1
    return False
        
if find_key(0, 3, mat, row, col) == True:
    print("found")
else:
    print("Not there")
