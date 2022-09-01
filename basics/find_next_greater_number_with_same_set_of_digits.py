n = "218765"
n = list(n)

prev = n[-1]
for i in reversed(range(len(n) - 1)):
    if n[i] >= prev:
        prev = n[i]
    else:
        print(n[i], prev)
        k = n[i]
        l = len(n) - 1
        print(i, l)
        while i < l:
            if n[i] > n[l]:
                l = l - 1
                print("".join(n))
            else:
                n[i], n[l] = n[l], n[i]
                i = l
        break
                
print("".join(n))
            
        
        
    


    
