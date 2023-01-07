class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        temp = ''.join(board)
        
        #players turn
        fr = Counter(temp)
        if fr['O'] > fr['X'] or fr['X'] - fr['O'] > 1: 
            return False
        
        
        #first move
        if temp.strip() == "O":
            return False  
        
        #check overlapping
        for mv in board:
            if len(mv) > 3:
                return False
        
        def winningChance(turn):
            # horizontal winn
            for i in range(len(board)):
                if board[i][0] == board[i][1] == board[i][2] == turn:
                    return True  

            # vertical winn
            for (a,b,c) in zip(*board):
                if a == b == c == turn:
                    return True

            #diagonal Win
            if board[0][0] == board[1][1] == board[2][2] == turn:
                return True

            elif board[0][2] == board[1][1] == board[2][0] == turn:
                return True

        
        if winningChance('X') and fr['X'] - fr['O'] != 1: ##case2
            return False
        if winningChance('O') and fr['X'] - fr['O'] != 0:
            return False

        return True
        
        
        