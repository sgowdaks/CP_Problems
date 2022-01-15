def reverse(st,le):
    l = []
    print(mainR(st,le,l,prefix = ""))

def mainR(st,n,l,prefix):
    if n < 1:
        return 
    if n == 1:
        for j in st:
            l.append(prefix+j)
 
    for i,val in enumerate(st):
        
        mainR(st,n-1,l,prefix+val)
        
    return l
        
        
st = "ab"
le = 3
reverse(st,le)
