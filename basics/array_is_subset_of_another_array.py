def isSubset( a1, a2, n, m):
    dicti = {}
    
    for i in a1:
        if i in dicti:
            dicti[i] +=1
        else:
            dicti[i] = 1
    
    for i in a2:
        if i not in dicti.keys():
            return "No"
        else:
            if dicti[i] == 0:
                return "No"
            else:
                dicti[i] -= 1
                    
    
    return "Yes"
