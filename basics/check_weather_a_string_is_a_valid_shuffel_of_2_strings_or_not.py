str1 = 'onetwofour'
str2 = 'hellofourtwooneworld'

s1 = len(str1)
if s1 > len(str2):
    print("not possible")
else:
    dicti = {}
    #dicti of string 1
    for i in str1:
        if i in dicti:
            dicti[i] += 1
        else:
            dicti[i] = 1
    #dicti of string 2
    dicti2 = {}
    str2 = list(str2)
    for i in range(0, len(str1)):
        if str2[i] in dicti2:
            dicti2[str2[i]] += 1
        else:
            dicti2[str2[i]] = 1
            
    print(dicti)
    print(dicti2)
            
    #cross check
    j = 0
    for i in range(s1, len(str2)):
        if dicti == dicti2:
            print(dicti2)
            print("found")
            break
        else:
            if str2[i] in dicti2:
                dicti2[str2[i]] += 1
            else:
                dicti2[str2[i]] = 1
            if dicti2[str2[j]] == 1:
                del dicti2[str2[j]]
            else:
                dicti2[str2[j]] -= 1
            j = j + 1
                
        
