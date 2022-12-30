class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        res = [[0 for _ in range(col)] for _ in range(row)]

        zerosRow = defaultdict(int)
        onesRow = defaultdict(int)
        
        zerosCol = defaultdict(int)
        onesCol = defaultdict(int)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 :
                    onesRow[i] += 1
                    onesCol[j] += 1
                    
                else:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
        
        for i in range(row):
            for j in range(col):
                
                diff = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
                res[i][j] = diff
        return res
        
        
        
        
        
        
        
        
        
        
        
#############################################################################################
        #for i in range(row):
            #onesRow = grid[i].count(1)
            #zerosRow = grid[i].count(0)
            #for j in range(col):
                #columns = list(zip(*grid))
                #onesCol = columns[j].count(1)
                #zerosCol = columns[j].count(0)
                
                #diff = onesRow + onesCol - zerosRow - zerosCol
                
                #res[i][j] = diff
        #return res
                
                
                
            