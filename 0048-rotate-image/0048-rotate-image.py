class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # if allocating another matrix was possible , 
        # first reverse the order of the rows
        # then transpose the matrix, but this wants new 2d matrix
        l,r = 0, len(matrix[0])-1
        
        while l < r:
            for i in range(r-l):
                top = l
                bottom = r
                temp = matrix[top][l + i]
                
                matrix[top][l + i] = matrix[bottom -i][l] 
                
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                matrix[bottom][r-i] = matrix[top + i][r]
                
                matrix[top + i][r] = temp
            l += 1
            r -= 1