def divideit(string1):
    i = 0
    while(i<len(string1)):
        #print(i)
        countz = 0
        counto = 0
        newstring = ""
        if(string1[i] == "0"):
            newstring += string1[i]
            countz = 1
        else:
            newstring += "1"
            counto = 1
        i = i+1    
        while(counto != countz and i<len(string1)):
            newstring += string1[i]
            #print(newstring)
            if(string1[i] == "0"):
                countz += 1
            else:
                counto += 1
            i = i+1
            #print(i)
        print(newstring)   
        
divideit("010011011")

    
    
            
        
        
    
            
            
            
            
