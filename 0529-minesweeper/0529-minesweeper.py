class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = len(board), len(board[0])
        directions = [(-1,0),(0,-1),(1,0),(0,1),(-1,1),(1,-1),(-1,-1),(1,1)]
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            
            if board[i][j] == 'M':
                board[i][j] = 'X'
                return
    
            if board[i][j] == 'E':
                temp = 0
                for l , k in directions:
                    if -1 < i+l < row and -1 < j+k < col:
                        if board[i+l][j+k] == 'M':
                            temp += 1

                if temp != 0:
                    board[i][j] = str(temp)
                else:
                    board[i][j] = 'B'
                    
                    for l , k in directions:
                        if -1 < i+l < row and -1 < j+k < col :
                            dfs(i+l,j+k)
        
        dfs(click[0],click[1])
        return board
                

