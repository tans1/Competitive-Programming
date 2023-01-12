class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if row[0] <= target <= row[-1]:
                break
        for nm in row:
            if nm == target:
                return True
        return False