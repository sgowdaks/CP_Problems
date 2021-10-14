string1 = "AACD"
string2 = "ACDA"

for i in range(1,len(string1)+1):
    newstring = string1[i:]+string1[:i]
    print(newstring)
    if(newstring == string2):
        print("yes")
        break
    
