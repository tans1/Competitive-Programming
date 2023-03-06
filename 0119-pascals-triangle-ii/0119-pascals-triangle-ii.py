class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def helper(row):
            if row == 0:
                return [1]
            elif row == 1:
                return [1,1]
            
            up_row = helper(row-1)
            n = len(up_row)
            temp = [1]
            for i in range(n-1):
                temp.append(up_row[i]+ up_row[i+1])
            temp.append(1)
            
            return temp
                
        return helper(rowIndex)
            