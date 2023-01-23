class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        newMatrix = [[0 for _ in range(c)] for _ in range(r)]
        
        temp = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp.append(mat[i][j])
            
        if r* c == len(mat) * len(mat[0]):
            k = 0
            for i in range(r):
                for j in range(c):
                    newMatrix[i][j] = temp[k]
                    k += 1
            return newMatrix
        
        else:
            return mat

        