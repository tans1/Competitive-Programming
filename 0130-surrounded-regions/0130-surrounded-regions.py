class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def dfs(i,j):
            if not ( 0 <= i < row and 0 <= j < col) or board[i][j] != "O":
                return 
            board[i][j] = 'T'
            for l,r in directions:
                dfs(i+l, j+r)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r in [0,row-1] or c in [0,col-1]):
                    dfs(r,c)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"
                    
            