class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        stack_memo = {}
        
        def heleper(l,r,turn):
            if l > r :
                return 0
            else:
                if (l,r,turn) in stack_memo:
                    return stack_memo[(l,r,turn)]
                else:
                    
                    if turn:
                        stack_memo[(l,r,turn)] = max(nums[l] + heleper(l+1, r, not turn),  nums[r] + heleper(l, r-1, not turn))

                    else:
                        stack_memo[(l,r,turn)] = min(-nums[l] + heleper(l+1, r, not turn),-nums[r] + heleper(l, r-1, not turn))
                    
                    return stack_memo[(l,r,turn)]
                
        return heleper(0,len(nums)-1,True) >= 0
            
                