list1 = []
        s = list(s)
        st = ""
        n = len(s)
        def permutation(s,list1, st, n):
            if len(s) == 0:
                list1.append(st)
                return None
            elif s[0].isalpha():
                permutation(s[1:],list1, st + (s[0].upper()), n)
                permutation(s[1:],list1, st + (s[0].lower()), n)
            else:
                permutation(s[1:],list1, st + s[0], n)
                
                
        permutation(s, list1, st, n)
        return list1
