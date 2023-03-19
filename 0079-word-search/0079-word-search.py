class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        prev = set()
        
        def backtracking(i,j,k):
            if k >= len(word):
                return True
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or  board[i][j] != word[k] or (i,j) in prev:
                return False
            
            prev.add((i,j))
            res = backtracking(i,j+1,k+1) or backtracking(i,j-1,k+1) or backtracking(i-1,j,k+1) or backtracking(i+1,j,k+1)
            
            prev.remove((i,j))
            return res
        

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtracking(i,j,0):
                    return True
        return False