class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def helper(i,j):
            
            cnt = 0
            
            #left
            l = j
            while l >= 0:
                if board[i][l] == '.' or board[i][l] == 'R' :
                    l -= 1
                elif board[i][l] == 'p':
                    cnt += 1
                    break
                elif board[i][l] == 'B':
                    break
            #right
            r = j
            while r < 8:
                if board[i][r] == '.' or board[i][r] == 'R':
                    r += 1
                elif board[i][r] == 'p':
                    cnt += 1
                    break
                elif board[i][r] == 'B':
                    break
                    
            #up
            u = i
            while u >= 0:
                if board[u][j] == '.' or board[u][j] == 'R':
                    u -= 1
                elif board[u][j] == 'p':
                    cnt += 1
                    break
                elif board[u][j] == 'B':
                    break
                    
            #down
            d = i
            while d < 8:
                if board[d][j] == '.' or board[d][j] == 'R':
                    d += 1
                elif board[d][j] == 'p':
                    cnt += 1
                    break
                elif board[d][j] == 'B':
                    break
            return cnt
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    cnt = helper(i,j)
                    break
        return cnt
                    