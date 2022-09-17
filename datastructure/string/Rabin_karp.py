txt = "GEEKS FOR GEEKS"
pat = "GEEK"

#Rabin Karp Algorithm
t = len(txt)
p = len(pat)

#check hash value for pattern
phash = 0
for i in pat:
    phash += ord(i) - 64
    
thash = 0
for i in range(p):
    thash += ord(txt[i]) - 64

i = 0
j = p
while j <= t:
    if phash == thash:
        print("found")
        break
    else:
        thash -= ord(txt[i])
        i = i - 1
        j = j + 1
        thash += ord(txt[i])

    
    
    
