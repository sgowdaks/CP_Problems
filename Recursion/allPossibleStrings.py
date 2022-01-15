def reverse(st):
    l = []
    print(mainR(st,len(st),l,prefix = ""))

def mainR(st,n,l,prefix):
    if n < 1:
        return 
    if n == 1:
        for j in st:
            l.append(prefix+j)

    for i,val in enumerate(st):
        
        mainR(st,n-1,l,prefix+val)
        
    return l
        
        
st = "abc"
reverse(st)
