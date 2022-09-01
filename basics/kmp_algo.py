sen = "badabbbada"
pattern = "bbada"

kmp_tabel = list(pattern)
pattern = list(pattern)

kmp_values = []
dicti = {}
for i in range(len(kmp_tabel)):
    if kmp_tabel[i] not in dicti:
        dicti[kmp_tabel[i]] = i 
        kmp_values.append(0)
    else:
        kmp_values.append(dicti[kmp_tabel[i]]+1)

sen = list(sen)
j = 0
print(sen)

i = 0

kmp_values = [None] + kmp_values

print(kmp_values)

kmp_tabel = [None] + kmp_tabel
pattern = [None] + pattern
print(kmp_tabel)

for i in range(len(sen)):
    print(i, j + 1,sen[i], pattern[j+1])
    if sen[i] == pattern[j+1]:
        j = j + 1
        if j > len(pattern):
            print(i)
            print("found!")
            break
    else:
        # print(i, j, sen[i], pattern[j])
        j = kmp_values[j+1]
        #again check the condition
        print(j)
        if j != 0:
            if sen[i] != pattern[j+1]:
                print("cross: ",sen[i], pattern[j+1])
                j = kmp_values[j]
                print("new j: ", j)
            
    
    

    
