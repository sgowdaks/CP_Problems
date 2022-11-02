class Solution:
    def minimumKeypresses(self, s: str) -> int:
        dicti = {}
        for i in s:
            if i in dicti:
                dicti[i] += 1
            else:
                dicti[i] = 1
        dicti = {k: v for k, v in sorted(dicti.items(), key=lambda item: item[1], reverse = True)}
        count = 0
        feq = 0
        for i, pair in enumerate(dicti.keys()):
            if i % 9 == 0:
                feq += 1
            
            count +=  (feq * dicti[pair])
        return count
