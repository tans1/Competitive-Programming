class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #first condition
        def checkHorizontal(board):
            for rw in board:
                frq = Counter(''.join(rw))

                for k,v in frq.items():
                    if k != '.' and v > 1:
                        return False
            return True
        
        def checkVerical(board):
            cols = list(zip(*board))       
            for i in range(len(board[0])):
                frq = Counter(''.join(cols[i]))
                for k,v in frq.items():
                    if k != '.' and v > 1:
                        return False
            return True
        
        def checkSubBox(board):
            i= 0
            while i < len(board):
                j = 0
                while j < len(board[0]):
                    temp = ""
                    for r in range(i,i+3):
                        for c in range(j,j+3):
                            temp += board[r][c]
                            
                    frq = Counter(''.join(temp))
                    for k,v in frq.items():
                        if k != '.' and v > 1:
                            return False
                    j += 3
                i += 3
            return True
        
        return checkHorizontal(board) and checkVerical(board) and checkSubBox(board)
        
            
        
        