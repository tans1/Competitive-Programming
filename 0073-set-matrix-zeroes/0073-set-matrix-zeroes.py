class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def makeZero(i,j):
            #make entire row = 0
            for c in range(len(matrix[0])):
                matrix[i][c] = 0
            
            #make entire column = 0
            for r in range(len(matrix)):
                matrix[r][j] = 0
            
        
        zeroIndex = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroIndex.append((i,j))
        
        for ind in zeroIndex:
            makeZero(ind[0],ind[1])
        
        
            