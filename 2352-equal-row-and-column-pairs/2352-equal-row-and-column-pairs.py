class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dc = defaultdict(int)
        
        for r in grid:
            row = list(map(lambda x:str(x),r))
            dc[' '.join(row)] += 1
            
        
        cnt = 0
        n = len(grid[0])
        col = list(zip(*grid))
        for i in range(n):
            column = list(map(lambda x:str(x), col[i]))
            cnt += dc[' '.join(column)]
        
        return cnt