class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        dct = {}
        for i in range(row):
            for j in range(col):
                if (i-j) not in dct:
                    dct[i-j] = matrix[i][j]
                
                else:
                    if dct[i-j] != matrix[i][j]:
                        return False
        return True