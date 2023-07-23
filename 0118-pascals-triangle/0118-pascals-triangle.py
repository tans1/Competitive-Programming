class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        dp = [[1],[1,1]]
        for _ in range(numRows - 2):
            temp = [1]
            for j in range(len(dp[-1])-1,0,-1):
                temp.append(dp[-1][j]+dp[-1][j-1])
            temp.append(1)
            dp.append(temp)
            
        return dp
        