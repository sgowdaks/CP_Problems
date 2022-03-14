class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s = s.split(":")
        a = s[0]
        b = s[1]
        output = []
        for i in range(ord(a[0]),ord(b[0])+1):
            for j in range(int(a[1]), int(b[1])+1):
                output.append(chr(i)+str(j))
        return output
