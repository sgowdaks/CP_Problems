def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        list1 = []
        pattern = list(pattern)
        for query in queries:
            list1.append(self.check(query,pattern))
        return list1
    
    def check(self, query, pattern):
        j = 0
        for i, val in enumerate(query):
            if j == len(pattern):
                if ord(val) >= 65 and ord(val) <=90:
                    return False
            else:   
                if ord(val) >= 65 and ord(val) <=90:
                    if val != pattern[j]:
                        return False
                if val == pattern[j]:
                    # print(val,pattern[j])
                    j = j + 1
                else:
                    pass
        if j == len(pattern):
            return True
        else:
            return False
                    
