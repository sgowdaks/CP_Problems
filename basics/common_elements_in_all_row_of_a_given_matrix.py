mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]
       
 
dicti = {} 
for i in mat[0]:
    if i not in dicti:
        dicti[i] = 0
    
for i in range(1, len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] in dicti and dicti[mat[i][j]] < i:
            dicti[mat[i][j]] += 1 

for i in dicti:
    if dicti[i] == (len(mat) - 1):
        print(i)
            
    
