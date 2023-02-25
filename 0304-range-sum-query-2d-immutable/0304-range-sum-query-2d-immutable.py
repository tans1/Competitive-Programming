class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # make prefix sums for rows
        for r in range(len(matrix)):
            for c in range(1, len(matrix[0])):
                matrix[r][c] += matrix[r][c - 1] 
                
        # make prefix sums for regions
        for r in range(1, len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] += matrix[r - 1][c]
        self.matrix = matrix
        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = self.matrix[row2][col2]
        
        if row1 != 0 and col1 != 0:
            origin = self.matrix[row1 - 1][col1 - 1] 
        else:
            origin = 0
        if col1 != 0:
            left = self.matrix[row2][col1 - 1] 
        else:
            left = 0
        if row1 != 0:
            top = self.matrix[row1 - 1][col2] 
        else:
            top = 0
        return region_sum - top - left + origin

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)