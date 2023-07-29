class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if  k == 0:
            return 1
            
        total = 8 ** k
        directions = [
            (-1,-2),(1,-2),(2,-1),(2,1),(-1,2),(1,2),(-2,-1),(-2,1)
        ]
        
        onBoard = 0
        
        memo = {}
        
        def dfs(row, col,moves):
            if not (0 <= row < n and 0 <= col < n):
                return 0
            
            if moves == 0:
                return 1
            if moves > 0:
                sm = 0
                
                for (x,y) in directions:
                    if (row+x, col+y, moves) not in memo:
                        memo[(row+x, col+y, moves)] = dfs(row+x, col+y, moves-1)
                    sm += memo[(row+x, col+y, moves)]
                return sm
            
        onBoard = dfs(row,column,k)        
        return onBoard / total
        
            
        