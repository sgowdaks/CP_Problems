class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) <= 2:
            return False
        colors = list(colors)
        flag = 1
        i = 1
        j = 1
        
        alice = 0
        while i + 1 < len(colors):
            if colors[i] == "A" and colors[i-1] == "A" and colors[i+1] == "A":
                del colors[i]
                alice += 1 
            else:
                i = i + 1
                
            
                
        bob = 0
        while j + 1  < len(colors):
            if colors[j] == "B" and colors[j-1] == "B" and colors[j+1] == "B":
                del colors[j]
                bob += 1
            else:
                j = j + 1
                
            if bob > alice:
                return False
                
                
        if alice == bob:
            return False
                
        return True
