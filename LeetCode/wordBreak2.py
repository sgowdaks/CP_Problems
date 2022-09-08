class Solution:
    def wordBreak(self, string: str, dicti: List[str]) -> List[str]:
        def wordB(string, dicti, list1, st):
            point = 0
            for i in range(0, len(string)+1):
                word = string[0:i] 
                if word in dicti:                     
                    if len(st) > 0:
                        st = st + " " + word
                        point = 1
                    else:
                        st = st + word                        
                    
                    if string[i:] == "":
                        list1.append(st)
                    else:    
                        wordB(string[i:], dicti, list1, st)
						            #to check the other part, we just remove what was concatenated previously
                        lis = list(st)
                        n = len(st)
                        w = len(word)
                        if point == 1:
                            w += 1
                        l = st[0:len(st)-w]
                        st = "".join(l)
                        point = 0
                                
        if len(string) == 1:
            if string in dicti:
                return dicti
            else:
                return []

            
        list1 = []
        st = ""
        wordB(string, dicti,list1, st)
        return list1
	
