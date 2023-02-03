class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid) -2):
            for j in range(len(grid[0]) -2):
                #horizontal
                first_row = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                second_row = grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2]
                third_row = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                #vertical
                first_col = grid[i][j] + grid[i+1][j] + grid[i+2][j]
                second_col = grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]
                third_col = grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2]
                #diagonal
                
                main_diagonal = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                diagonal2 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
                
                if first_row == second_row == third_row == first_col == second_col == third_col == main_diagonal == diagonal2:
                    temp = []
                    temp.extend(grid[i][j:j+3])
                    temp.extend(grid[i+1][j:j+3])
                    temp.extend(grid[i+2][j:j+3])
                    temp2 = Counter(temp)
                    if len(temp2) == 9:
                        flag = False
                        for n in list(temp2.keys()):
                            if n > 9 or n < 1:
                                flag = True
                        if not flag:
                            cnt += 1
        return cnt
                    
                