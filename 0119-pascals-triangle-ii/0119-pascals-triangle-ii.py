class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def helper(row):
            if row == 0:
                return [1]
            elif row == 1:
                return [1,1]
            
            up_row = helper(row-1)
            n = len(up_row)
            res = [1]
            
            for i in range(n-1):
                res.append(up_row[i]+ up_row[i+1])
            res.append(1)
            
            return res
                
        return helper(rowIndex)
            