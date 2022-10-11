class Solution:
    def find_permutation(self, S):
        S = list(S)
        n = len(S)
        arr = []
        
        def permutataion(S, arr, n, st):
            if len(S) == 1:
                arr.append(st+S[0])
                return
                
            for i in range(len(S)):
                s = S[:i] + S[i+1:]
                # print(s)
                permutataion(s, arr, n, st = st + S[i])
        
        permutataion(S, arr, n, st = "")
        
        return sorted(set(arr))
