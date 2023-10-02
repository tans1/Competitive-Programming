class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice , bob = 0, 0
        i = 1
        j = 0
        while i < len(colors) and j < len(colors):
            while i < len(colors) and colors[i] == colors[i-1]:
                i += 1
            if i - j > 2:
                if colors[i-1] == "A":
                    alice += (i-j) - 2

                else:
                    bob += (i-j) - 2
            j = i
            i += 1
        if i - j > 2:
            if colors[i-1] == "A":
                alice += (i-j) - 2
                
            else:
                bob += (i-j) - 2
        
        return alice > bob
                
            
            
            
        