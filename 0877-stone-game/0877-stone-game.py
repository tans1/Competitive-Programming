class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        stack_memo = {}
        
        def helper(l,r, turn):
            if l > r:
                return 0
            else:
                if (l,r,turn) not in stack_memo:
                    
                    if turn: # alice turn
                        choice1 = piles[l] + helper(l+1, r, not turn)
                        choice2 = piles[r] + helper(l, r-1, not turn)

                        stack_memo[(l,r,turn)] = max(choice1, choice2)

                    else:
                        choice1 = -piles[l] + helper(l+1, r, not turn)
                        choice2 = -piles[r] + helper(l, r-1, not turn)

                        stack_memo[(l,r,turn)] =  min(choice1, choice2)
                    
                return stack_memo[(l,r,turn)]
            
        return helper(0,len(piles)-1, True) > 0
