class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if row[0] <= target <= row[-1]:
                break
        for nm in row:
            if nm == target:
                return True
        return False
        
        
        
        
        
        
        # i = 0
        # cl = len(matrix[0])-1
        # while i < len(matrix) and target not in matrix[i]:
        #     i += 1
        # if i < len(matrix) and target in matrix[i]:
        #     return True
        # return False
        
            