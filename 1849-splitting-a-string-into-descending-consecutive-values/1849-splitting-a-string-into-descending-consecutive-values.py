class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def backtracking(prev, prevIndex): # it will be easier by drawing the recursion tree
            if prevIndex >= n:
                return True
            
            for j in range(prevIndex,n):
                temp = int(s[prevIndex:j+1])
                
                if prev == temp + 1 and backtracking(temp, j+1):
                    return True
            return False
        
        
        
        for i in range(n-1):
            cur = int(s[:i+1])
            
            if backtracking(cur, i+1):
                return True
        
        return False
        
        
        
        